# HTakeNote

HTakeNote is a minimal Flask application for jotting down quick notes. It exposes a single-page UI backed by SQLite via SQLAlchemy, and it is ready to deploy to Heroku using the supplied `Procfile` and Bitbucket pipeline configuration.

## Features
- Add, update, and delete text notes from a simple web interface.
- SQLite persistence managed through SQLAlchemy's ORM layer.
- Production entry point via Gunicorn and a Heroku `Procfile`.
- Lightweight test scaffold with pytest and pytest-flask.

## Tech Stack
- Python 3.9
- Flask 2 & Flask-SQLAlchemy
- SQLite
- Gunicorn (production WSGI server)
- pytest / flake8 (testing & linting)

## Getting Started

### Prerequisites
- Python 3.9 (matches `runtime.txt`)
- `pip` and `virtualenv`
- macOS/Linux shell or Windows WSL/PowerShell

You can run `scripts/1_setup_env.sh` for an automated check that Python and virtualenv are available and to scaffold a virtual environment named `venv`.

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
