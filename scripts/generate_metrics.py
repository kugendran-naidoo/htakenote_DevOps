import os, sys, json, math
from datetime import datetime, timedelta, timezone
import requests
import matplotlib.pyplot as plt

OWNER = os.environ.get("OWNER")
REPO  = os.environ.get("REPO")
TOKEN = os.environ.get("GH_TOKEN")

if not all([OWNER, REPO, TOKEN]):
    print("Missing OWNER/REPO/GH_TOKEN")
    sys.exit(1)

API = "https://api.github.com"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}
STAR_HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3.star+json"  # includes starred_at
}

os.makedirs("metrics", exist_ok=True)

def get(url, headers=HEADERS, params=None):
    r = requests.get(url, headers=headers, params=params, timeout=30)
    r.raise_for_status()
    return r.json()

def daterange(days):
    today = datetime.now(timezone.utc).date()
    return [today - timedelta(days=i) for i in range(days-1, -1, -1)]

def group_by_day(timestamps):
    # returns dict {date: count}
    g = {}
    for ts in timestamps:
        d = datetime.fromisoformat(ts.replace("Z","+00:00")).date()
        g[d] = g.get(d, 0) + 1
    return g

# --------- fetch data ----------
# 1) Clones & views: last 14 days only
traffic_clones = get(f"{API}/repos/{OWNER}/{REPO}/traffic/clones")
traffic_views  = get(f"{API}/repos/{OWNER}/{REPO}/traffic/views")
clones_points = {datetime.fromisoformat(p["timestamp"].replace("Z","+00:00")).date(): p["count"] for p in traffic_clones.get("clones", [])}
views_points  = {datetime.fromisoformat(p["timestamp"].replace("Z","+00:00")).date(): p["count"] for p in traffic_views.get("views", [])}

# 2) Stars timeline
# paginated; pull first few pages (enough for small repos)
stars = []
page = 1
while True:
    data = requests.get(f"{API}/repos/{OWNER}/{REPO}/stargazers", headers=STAR_HEADERS, params={"per_page":100, "page":page}, timeout=30)
    if data.status_code == 204 or data.status_code == 404:
        break
    data.raise_for_status()
    payload = data.json()
    if not payload:
        break
    stars.extend(payload)
    if len(payload) < 100 or page >= 10:  # cap pages
        break
    page += 1
star_times = [s["starred_at"] for s in stars]

# 3) Forks timeline
forks = []
page = 1
while True:
    payload = get(f"{API}/repos/{OWNER}/{REPO}/forks", params={"per_page":100, "page":page})
    if not payload:
        break
    forks.extend(payload)
    if len(payload) < 100 or page >= 10:
        break
    page += 1
fork_times = [f["created_at"] for f in forks]

# 4) Commits last 30 days (count per day)
since = (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
commits = []
page = 1
while True:
    payload = get(f"{API}/repos/{OWNER}/{REPO}/commits", params={"since": since, "per_page":100, "page":page})
    if not payload:
        break
    commits.extend(payload)
    if len(payload) < 100 or page >= 10:
        break
    page += 1
commit_times = [c["commit"]["author"]["date"] for c in commits if c.get("commit",{}).get("author")]

# --------- build series ----------
last14 = daterange(14)
last30 = daterange(30)
def series_from_points(dates, values_dict):
    return [values_dict.get(d, 0) for d in dates]

clones_series = series_from_points(last14, clones_points)
views_series  = series_from_points(last14, views_points)

stars_by_day = group_by_day(star_times)
forks_by_day = group_by_day(fork_times)
commits_by_day = group_by_day(commit_times)

stars_cumulative = []
forks_cumulative = []
cum = 0
for d in last30:
    cum += stars_by_day.get(d, 0)
    stars_cumulative.append(cum)
cum = 0
for d in last30:
    cum += forks_by_day.get(d, 0)
    forks_cumulative.append(cum)
commits_series = [commits_by_day.get(d, 0) for d in last30]

# --------- plot helpers ----------
def save_line_chart(dates, yseries_list, labels, title, outfile):
    plt.figure(figsize=(9, 3))
    for y, label in zip(yseries_list, labels):
        plt.plot(dates, y, label=label)
    plt.title(title)
    plt.xlabel("Date")
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.tight_layout()
    if len(yseries_list) > 1:
        plt.legend(loc="upper left", fontsize=8)
    plt.savefig(outfile, dpi=160)
    plt.close()

# --------- render charts ----------
# traffic (14d)
save_line_chart(last14, [clones_series, views_series], ["clones", "views"],
                f"Traffic (last 14 days) — {OWNER}/{REPO}",
                "metrics/traffic_14d.png")

# commits (30d)
save_line_chart(last30, [commits_series], ["commits/day"],
                f"Commits (last 30 days) — {OWNER}/{REPO}",
                "metrics/commits_30d.png")

# stars & forks (30d cumulative)
save_line_chart(last30, [stars_cumulative, forks_cumulative], ["stars (cum)", "forks (cum)"],
                f"Stars & Forks (last 30 days, cumulative) — {OWNER}/{REPO}",
                "metrics/stars_forks_30d.png")

print("Wrote: metrics/traffic_14d.png, metrics/commits_30d.png, metrics/stars_forks_30d.png")
