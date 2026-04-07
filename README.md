# To-Do App

A Flask to-do list application with SQLite persistence, task filtering, tags, and Docker support.

## Features

- Create, edit, and delete tasks
- Mark tasks complete or incomplete
- Search, filter, and sort tasks
- Track priority, due date, and status
- Manage tags for tasks
- Expose runtime version information at `/api/version`

## Requirements

- Docker
- Docker Compose
- Python 3.11+ for local development

## Run with Docker

```bash
docker-compose up --build
```

Open http://localhost:5000 when the container is running.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The app creates `todo.db` automatically on startup.

## Tests

The CI workflow installs `pytest` and `pytest-flask`, then runs:

```bash
pytest --tb=short -v
```

## API

- `GET /api/version` returns version and status data.
- `POST /add` adds a task.
- `GET /edit/<id>` and `POST /edit/<id>` edit a task.
- `GET /delete/<id>` deletes a task.
- `POST /toggle/<id>` toggles completion.
- `GET /tags` lists tags.

## Project Structure

- `app.py` Flask application and SQLite setup
- `templates/` HTML templates
- `tests/` automated tests
- `Dockerfile` container image definition
- `docker-compose.yml` local container configuration

## Versioning

Set `APP_VERSION` to override the version returned by `/api/version`.
