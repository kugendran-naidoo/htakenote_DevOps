# 🧠 HTakeNote

> 🚀 **HTakeNote** is a minimal Flask application for jotting down quick notes — ready to deploy on Heroku and optimized for simplicity, clarity, and quick DevOps integration.

## 📊 Traffic & Popularity
![Clones](https://img.shields.io/endpoint?cacheSeconds=300&url=https%3A%2F%2Fgist.githubusercontent.com%2Fkugendran-naidoo%2F2b0de4f9f92a605b780e986e6d48ffcc%2Fraw%2Fhtakenote_DevOps-clones.json%3Fv%3D2)
![Views](https://img.shields.io/endpoint?cacheSeconds=300&url=https%3A%2F%2Fgist.githubusercontent.com%2Fkugendran-naidoo%2F9b749f24de62343dc995f8d524027c39%2Fraw%2Fhtakenote_DevOps-views.json%3Fv%3D2)
![Stars](https://img.shields.io/endpoint?cacheSeconds=300&url=https%3A%2F%2Fgist.githubusercontent.com%2Fkugendran-naidoo%2F2b0de4f9f92a605b780e986e6d48ffcc%2Fraw%2Fhtakenote_DevOps-stars.json%3Fv%3D2)
![Commits](https://img.shields.io/endpoint?cacheSeconds=300&url=https%3A%2F%2Fgist.githubusercontent.com%2Fkugendran-naidoo%2F2b0de4f9f92a605b780e986e6d48ffcc%2Fraw%2Fhtakenote_DevOps-commits.json%3Fv%3D2)

> Auto-updated daily at 14:00 UTC via GitHub Actions.

## 📈 Metrics
![Activity (last 4 weeks)](https://raw.githubusercontent.com/kugendran-naidoo/htakenote_DevOps/main/metrics/activity_4w.png)

<!--![Forks](https://img.shields.io/github/forks/kugendran-naidoo/htakenote_DevOps?style=social)
![Issues](https://img.shields.io/github/issues/kugendran-naidoo/htakenote_DevOps)
![License](https://img.shields.io/github/license/kugendran-naidoo/htakenote_DevOps)
![Last Commit](https://img.shields.io/github/last-commit/kugendran-naidoo/htakenote_DevOps)

![Traffic 14d](https://raw.githubusercontent.com/kugendran-naidoo/htakenote_DevOps/main/metrics/traffic_14d.png)
![Commits 30d](https://raw.githubusercontent.com/kugendran-naidoo/htakenote_DevOps/main/metrics/commits_30d.png)
![Stars & Forks 30d](https://raw.githubusercontent.com/kugendran-naidoo/htakenote_DevOps/main/metrics/stars_forks_30d.png)

[![Star History](https://api.star-history.com/svg?repos=kugendran-naidoo/htakenote_DevOps&type=Date)](https://star-history.com/#kugendran-naidoo/htakenote_DevOps)-->

---

## ✨ Features
- 📝 Add, update, and delete text notes from a single-page web UI.
- 💾 SQLite persistence powered by SQLAlchemy’s ORM layer.
- ☁️ Production-ready via Gunicorn and a Heroku `Procfile`.
- 🔧 CI/CD with Bitbucket pipelines for test, lint, and deploy.
- 🧪 Lightweight test scaffold using `pytest` and `pytest-flask`.

---

## ⚙️ Tech Stack
- **Python 3.9**
- **Flask 2 & Flask-SQLAlchemy**
- **SQLite**
- **Gunicorn** (production WSGI server)
- **pytest / flake8** (testing & linting)

---

## ⚡ Quickstart

### Prerequisites
- Python 3.9 (matches `runtime.txt`)
- `pip` and `virtualenv`
- macOS/Linux shell or Windows WSL/PowerShell

Automated environment setup:
```bash
scripts/1_setup_env.sh
```


### Local Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Running the Application
```bash
# From the repository root
export PYTHONPATH=src
flask --app app --debug run

# Alternative: cd src && python app.py
```
The first run will create `src/notes.db` automatically. The development server listens on http://127.0.0.1:5000/ by default.

### Running Tests
```bash
export PYTHONPATH=src
pytest -v tests/test_app.py
```

### Code Style & Linting
The Bitbucket pipeline uses flake8. You can mirror it locally:
```bash
flake8 --per-file-ignores="test_app.py:F401" . --extend-exclude=dist,build --show-source --statistics
```

## Project Structure
```
.
├── Procfile                  # Heroku entry point (Gunicorn)
├── README.md
├── bitbucket-pipelines.yml   # CI pipeline (tests + lint + deploy)
├── requirements.txt
├── runtime.txt               # Python runtime spec for Heroku
├── scripts/
│   └── 1_setup_env.sh        # Helper for local env bootstrap
├── src/
│   ├── app.py                # Flask application and data model
│   ├── notes.db              # SQLite database (auto-created)
│   ├── static/css/main.css   # Styling for the UI
│   └── templates/            # Jinja2 templates (base, index, update)
└── tests/
    └── test_app.py           # pytest scaffold
```

## Deployment
- The application is configured for Heroku deployment via the supplied `Procfile` (`web gunicorn --pythonpath src app:app`).
- Update Bitbucket repository variables `HEROKU_APP_TOKEN` and `HEROKU_APP_NAME`, then run the pipeline step "Deploy to Heroku Test" to push to Heroku.
- Ensure the Heroku app uses a persistent SQLite add-on or migrate to a managed database for production workloads.

## Contributing
1. Fork and clone the repository.
2. Create a virtual environment and install dependencies.
3. Run the automated tests before submitting changes.
4. Open a pull request with a clear description of your update.

## License
No explicit license is provided. If you intend to use this project in production or redistribute it, please contact the repository owner to clarify licensing terms.
