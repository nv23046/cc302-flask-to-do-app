# Final Submission — GitHub Actions CI/CD (Strict Checklist)

## Student Details
- Student ID: nv23046
- Course: CC312/CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- Branch: main

## Included Workflow Files
- CI workflow: [.github/workflows/ci.yml](.github/workflows/ci.yml)
- CD workflow: [.github/workflows/cd.yml](.github/workflows/cd.yml)

## Part A — CI Evidence (Required)

### A1) CI workflow file screenshot
- Screenshot must show:
  - trigger on `push` + `pull_request` for `main` and `dev`
  - `actions/setup-python@v5`
  - lint step (`flake8`)
  - test step (`pytest`)

### A2) Successful CI run (green)
- Screenshot: Actions → CI run details with overall green status.

### A3) Failed CI run (red)
- Screenshot: Actions → CI run details with red status and failing step log.

### A4) Fixed CI run (green again)
- Screenshot: Actions → next CI run after fix with green status.

## Part B — CD Evidence (Required)

### B1) CD workflow file screenshot
- Screenshot must show:
  - trigger on `release` with `types: [published]`
  - DockerHub login using secrets
  - version extraction from tag
  - build & push tags (version + latest)

### B2) Successful CD run (green)
- Screenshot: Actions → CD run details showing success for a published release.

### B3) Registry image tag screenshot
- Screenshot: DockerHub/ECR showing newly published tag matching release version.

## Part C — End-to-End Evidence (Required)

### C1) Release page screenshot
- Screenshot: GitHub Release page for new version (e.g., `v0.3.0`).

### C2) Matching registry tag screenshot
- Screenshot: same version tag visible in DockerHub/ECR.

## Secrets Verification (Required, no secret values)
- `DOCKERHUB_USERNAME` configured in GitHub repo secrets.
- `DOCKERHUB_TOKEN` configured in GitHub repo secrets.
- No secret values stored in repository files.

## Reflection (Ready to submit)
Using GitHub Actions helped me automate quality checks and deployment steps so I no longer rely on manual commands for every change. The CI workflow gave immediate feedback on lint and tests, which made it easier to catch issues before merging to main. The CD workflow connected releases to container publishing, so each release tag produced a matching Docker image tag automatically. I also learned the importance of GitHub Secrets for secure credentials and the difference between a failing and fixed pipeline run as evidence of troubleshooting. Overall, automation made my workflow faster, more reliable, and easier to reproduce.

## Final Marking Checklist
- [ ] CI workflow file shown
- [ ] CI green run screenshot
- [ ] CI red run screenshot
- [ ] CI fixed-green screenshot
- [ ] CD workflow file shown
- [ ] CD green run screenshot
- [ ] Registry tag screenshot
- [ ] Release page screenshot
- [ ] Reflection included
- [ ] Submitted PDF/Markdown
