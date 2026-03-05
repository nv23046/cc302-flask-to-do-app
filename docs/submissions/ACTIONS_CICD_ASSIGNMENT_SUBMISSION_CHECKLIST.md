# Actions CI/CD Assignment Submission Checklist

## Student Information
- Student ID: `nv23046`
- Course: `CC312/CC302`
- Repository: `https://github.com/nv23046/cc302-flask-to-do-app`
- Branch: `main`
- Submission Date: `2026-03-05`

## Implemented Files (In This Repo)
- CI workflow: `.github/workflows/ci.yml`
- CD workflow: `.github/workflows/cd.yml`
- Smoke tests: `tests/test_app.py`
- CRUD tests: `tests/test_crud.py`
- Test package init: `tests/__init__.py`

## Part A: CI Workflow (Continuous Integration)
- [x] Trigger configured on `push` to `main` and `dev`
- [x] Trigger configured on `pull_request` to `main` and `dev`
- [x] Checkout step present (`actions/checkout@v4`)
- [x] Python setup step present (`actions/setup-python@v5`, Python `3.11`)
- [x] Dependency install step present (`pip install -r requirements.txt`)
- [x] Lint step present (`flake8 app.py tests --count --max-line-length=120 --statistics`)
- [x] Test step present (`pytest tests/ -v --cov=app`)
- [x] At least one real app test present (`tests/test_app.py`)

### CI Evidence Required For Submission
- [ ] Screenshot: successful CI run (green) in GitHub Actions tab
- [ ] Screenshot: failed CI run (red), then fixed
- [ ] Paste/attach `ci.yml` in submission document

### CI Run Links (Generated)
- Failed CI run (red): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22714679433
- Fixed CI run (green): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22714700507

### How To Generate The Required Failed CI Screenshot
1. Create a temporary branch from `dev`.
2. Intentionally add a lint error in `tests/test_app.py` (for example: add trailing spaces).
3. Commit and push to `dev`.
4. Capture the red CI run screenshot from Actions.
5. Fix the lint error and push again.
6. Capture the green CI run screenshot from Actions.

### Quick Commands Used Locally (Verified)
```bash
python -m flake8 app.py tests --count --max-line-length=120 --statistics
PYTHONPATH=. python -m pytest tests/ -v --cov=app
```

## Part B: CD Workflow (Continuous Delivery)
- [x] Trigger configured on GitHub Release publish (`release.types: [published]`)
- [x] Checkout step present (`actions/checkout@v4`)
- [x] Docker Buildx step present (`docker/setup-buildx-action@v3`)
- [x] DockerHub login present using secrets (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`)
- [x] Version extraction from release tag present (`refs/tags/vX.Y.Z` -> `X.Y.Z`)
- [x] Docker push step present (`docker/build-push-action@v5`)
- [x] Version and `latest` image tags configured

### CD Evidence Required For Submission
- [ ] Screenshot: successful CD run (green)
- [ ] Screenshot: DockerHub (or ECR) showing new image tag
- [ ] Paste/attach `cd.yml` in submission document

### CD Run Links (Generated)
- Failed CD run (v0.3.0): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22714820237
- Failed CD run (v0.3.4): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22715547246
- Successful CD run (v0.3.5): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22715610836
- Release page (v0.3.5): https://github.com/nv23046/cc302-flask-to-do-app/releases/tag/v0.3.5

## Part C: End-to-End Flow Evidence
- [ ] Small change committed and pushed to `dev`
- [ ] CI run on `dev` is green
- [ ] PR opened from `dev` to `main`
- [ ] PR merged to `main`
- [x] New release published (example: `v0.3.0`)
- [x] CD run triggered and green
- [ ] Registry shows matching image tag (`0.3.0`)

### Deliverables For Part C
- [ ] 3-5 sentence flow summary
- [ ] Screenshot: release page showing new version
- [ ] Screenshot: registry page showing new tag

## Secrets Checklist (Do Not Expose Values)
- [x] `DOCKERHUB_USERNAME` created in GitHub repo secrets
- [x] `DOCKERHUB_TOKEN` created in GitHub repo secrets
- [ ] No secrets committed in repository files

## Final Submission Package Checklist
- [ ] CI workflow file (`ci.yml`) + successful CI screenshot
- [ ] CD workflow file (`cd.yml`) + successful CD screenshot
- [ ] Failed CI screenshot and fixed CI screenshot
- [ ] DockerHub/ECR screenshot with new image tag
- [ ] GitHub Release screenshot
- [ ] Reflection paragraph (what you learned)
- [ ] Single final PDF or Markdown assembled and submitted

## Reflection Template (Fill and Use)
I implemented GitHub Actions CI/CD to automate testing and Docker image delivery for my Flask ToDo app. The CI workflow now checks lint and runs tests on every push and pull request to `main` and `dev`, which helped catch issues early. The CD workflow runs on release publish, extracts the semantic version from the release tag, and pushes both versioned and `latest` Docker images using GitHub Secrets. This assignment showed me how automation improves reliability, speed, and consistency compared with manual deployment.

## Exact Files To Include In Your Submission
- `.github/workflows/ci.yml`
- `.github/workflows/cd.yml`
- `tests/test_app.py`
- Screenshots listed above
