# Actions CI/CD Assignment Final Submission

## Student Information
- Student ID: `nv23046`
- Course: `CC312/CC302`
- Repository: `https://github.com/nv23046/cc302-flask-to-do-app`
- Branch: `main`
- Submission Date: `2026-03-05`

## Part A: CI Workflow (Continuous Integration)
### Requirements Status
- [x] Trigger configured on push to `main` and `dev`
- [x] Trigger configured on pull request to `main` and `dev`
- [x] Checkout step present (`actions/checkout@v4`)
- [x] Python setup step present (`actions/setup-python@v5`, Python 3.11)
- [x] Dependency install step present
- [x] Lint step present
- [x] Test step present
- [x] At least one real app test present (`tests/test_app.py`)

### CI Evidence
- Successful CI run (green):
  - Link: `https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22714700507`
  - Screenshot: <img width="975" height="319" alt="image" src="https://github.com/user-attachments/assets/919e26e2-3574-480e-89d7-6c4a004982d7" />


- Failed CI run (red):
  - Link: `https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22714679433`
  - Screenshot: <img width="975" height="342" alt="image" src="https://github.com/user-attachments/assets/07d94742-bfc9-4ffe-8482-e13b629185ae" />


- Fixed CI run (green again):
  - Link: `https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22714700507`
  - Screenshot: <img width="975" height="314" alt="image" src="https://github.com/user-attachments/assets/687c0143-5a6c-4d22-b273-11d55f548a69" />


### CI Workflow File (`.github/workflows/ci.yml`)
```yaml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main, dev]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install flake8 pytest pytest-cov

      - name: Lint
        run: |
          flake8 app.py tests --count --max-line-length=120 --statistics

      - name: Run tests
        env:
          PYTHONPATH: .
        run: |
          pytest tests/ -v --cov=app
```

## Part B: CD Workflow (Continuous Delivery)
### Requirements Status
- [x] Trigger configured on release publish (`types: [published]`)
- [x] Docker Buildx setup present
- [x] DockerHub login via secrets present
- [x] Version extraction from tag present
- [x] Build and push with version tag and `latest` present

### CD Evidence
- Successful CD run (green):
  - Link: `https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22715610836`
  - Screenshot: <img width="975" height="298" alt="image" src="https://github.com/user-attachments/assets/819cc71f-3a67-4fa6-b9c4-a5aefdc44383" />


- Release page:
  - Link: `https://github.com/nv23046/cc302-flask-to-do-app/releases/tag/v0.3.5`
  - Screenshot: <img width="975" height="397" alt="image" src="https://github.com/user-attachments/assets/bba783bd-1514-4d12-8de8-3a1ba07d6833" />


- DockerHub tags:
  - Expected tags shown: `0.3.5`, `latest`
  - Screenshot: <img width="975" height="427" alt="image" src="https://github.com/user-attachments/assets/b3925acb-531f-4a52-98e4-c282da7db3e6" />


### CD Workflow File (`.github/workflows/cd.yml`)
```yaml
name: CD

on:
  release:
    types: [published]

jobs:
  build-push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to DockerHub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Extract version
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: |
            ${{ secrets.DOCKERHUB_USERNAME }}/todo-saas:${{ steps.version.outputs.VERSION }}
            ${{ secrets.DOCKERHUB_USERNAME }}/todo-saas:latest
```

## Part C: End-to-End Flow Summary (3-5 sentences)
I updated the repository workflows and tests so CI could run linting and automated tests on every push and pull request. I validated CI behavior with a failed run and then a fixed successful run as troubleshooting evidence. After configuring and verifying GitHub Secrets for DockerHub credentials, I published release `v0.3.5` to trigger CD. The CD workflow completed successfully and pushed both `0.3.5` and `latest` tags to DockerHub. This demonstrates full automation from code changes to released container images.

## Reflection
I implemented GitHub Actions CI/CD to automate testing and Docker image delivery for my Flask ToDo app. The CI workflow runs lint and tests automatically, which helped detect and fix issues quickly. I connected GitHub Releases to Docker image publishing with secure GitHub Secrets. Completing this pipeline improved reliability and made the release process reproducible and faster than manual deployment.

## Required Test File (`tests/test_app.py`)
```python
import app as app_module


def test_app_import():
    assert app_module.app is not None


def test_app_responds(tmp_path):
    """Smoke test: app responds to index route."""
    test_db = tmp_path / "test_todo.db"
    app_module.DATABASE = str(test_db)
    app_module.init_db()

    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        response = client.get("/")
    assert response.status_code in [200, 302]
```

## Submission Checklist
- [x] CI workflow included
- [x] CD workflow included
- [x] Failed CI and fixed CI run links included
- [x] Successful CD run and release links included
- [x] Reflection included
- [ ] Screenshots pasted in marked placeholders
- [ ] Exported to final Word/PDF and submitted
