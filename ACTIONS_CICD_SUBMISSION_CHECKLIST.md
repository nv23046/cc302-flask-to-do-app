# GitHub Actions CI/CD Assignment Submission Checklist

## Student / Repo

- Student ID: nv23046
- Course: CC312/CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- Branch: main

## Part A — CI Workflow (Continuous Integration)

### Required CI workflow file

- [ ] CI workflow file created: [.github/workflows/ci.yml](.github/workflows/ci.yml)

### CI trigger requirements

- [ ] Trigger on push to `main` and `dev`
- [ ] Trigger on pull request to `main` and `dev`

### CI job steps (must be present)

- [ ] Checkout code (`actions/checkout@v4`)
- [ ] Setup Python 3.11 (`actions/setup-python@v5`)
- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] Install test/lint tooling (`pytest`, `flake8`)
- [ ] Lint step added (`flake8`)
- [ ] Test step added (`pytest`)

### CI evidence to attach

- [ ] Screenshot: successful CI run (green)
- [ ] Screenshot: failed CI run (red)
- [ ] Screenshot: fixed CI run (green again)

## Part B — CD Workflow (Continuous Delivery)

### Required CD workflow file

- [ ] CD workflow file created: [.github/workflows/cd.yml](.github/workflows/cd.yml)

### CD trigger requirements

- [ ] Trigger on GitHub release publish (`on: release`, `types: [published]`)

### CD job steps (DockerHub path)

- [ ] Checkout code (`actions/checkout@v4`)
- [ ] Setup Docker Buildx (`docker/setup-buildx-action@v3`)
- [ ] Login using GitHub Secrets (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`)
- [ ] Extract version from release tag (e.g., `v0.2.0 -> 0.2.0`)
- [ ] Build and push image with version tag
- [ ] Push `latest` tag

### CD evidence to attach

- [ ] Screenshot: successful CD run (green)
- [ ] Screenshot: registry (DockerHub/ECR) showing new image tag

## Part C — End-to-End Flow

### Flow checklist

- [ ] Small change made in code
- [ ] Pushed to `dev` (CI passed)
- [ ] PR opened from `dev` to `main`
- [ ] PR merged to `main`
- [ ] New GitHub release published (e.g., `v0.3.0`)
- [ ] CD workflow ran and passed
- [ ] New image tag visible in registry

### End-to-end evidence to attach

- [ ] Screenshot: GitHub Release page (new version)
- [ ] Screenshot: registry with matching new tag

## Secrets Verification (Do not expose values)

- [ ] `DOCKERHUB_USERNAME` added in repo secrets
- [ ] `DOCKERHUB_TOKEN` added in repo secrets
- [ ] No secrets committed in code/workflow files

## Files to include in submission

- [ ] CI workflow file: [.github/workflows/ci.yml](.github/workflows/ci.yml)
- [ ] CD workflow file: [.github/workflows/cd.yml](.github/workflows/cd.yml)
- [ ] Screenshot: successful CI run
- [ ] Screenshot: failed CI run then fixed
- [ ] Screenshot: successful CD run
- [ ] Screenshot: DockerHub/ECR tag
- [ ] Screenshot: GitHub Release page
- [ ] Reflection paragraph included

## Ready-to-use Reflection (3–5 sentences)

Using GitHub Actions helped me automate quality checks and deployment steps so I no longer rely on manual commands for every change. The CI workflow gave immediate feedback on lint and tests, which made it easier to catch issues before merging to main. The CD workflow connected releases to container publishing, so each release tag produced a matching Docker image tag automatically. I also learned the importance of GitHub Secrets for secure credentials and the difference between a failing and fixed pipeline run as evidence of troubleshooting. Overall, automation made my workflow faster, more reliable, and easier to reproduce.

## Final submission status

- [ ] Final PDF/Markdown assembled with all required screenshots
- [ ] All links checked and working
- [ ] Submitted
