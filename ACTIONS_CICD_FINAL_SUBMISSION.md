# Final Submission — GitHub Actions CI/CD (Strict Checklist)

## Student Details
- Student ID: nv23046
- Course: CC312/CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- Branch: main

## Included Workflow Files
- CI workflow: [.github/workflows/ci.yml](.github/workflows/ci.yml)
- CD workflow: [.github/workflows/cd.yml](.github/workflows/cd.yml)

## Verified CI Run Links (Use these)
- CI success (green): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22542450801
- CI failed (red): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22542415824
- CI intentional failed (red): https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22542411209

## Part A — CI Evidence (Required)

### A1) CI workflow file screenshot
- Screenshot must show:
  - trigger on `push` + `pull_request` for `main` and `dev`
  - `actions/setup-python@v5`
  - lint step (`flake8`)
  - test step (`pytest`)

### A2) Successful CI run (green)
- Screenshot: open the green run link above and capture:
  - workflow name `CI`
  - commit title `ci: set PYTHONPATH for pytest module imports`
  - green status `Success`
  - passed lint and test steps

### A3) Failed CI run (red)
- Screenshot: open the failed run link above and capture:
  - red status `Failure`
  - failing step log (error shown)

### A4) Fixed CI run (green again)
- Use the same green run in A2 (it is the post-fix run).

## Part B — CD Evidence (Required)

### B1) CD workflow file screenshot
- Screenshot must show:
  - trigger on `release` with `types: [published]`
  - DockerHub login using secrets
  - version extraction from tag
  - build & push tags (version + latest)

### B2) Successful CD run (green)
- Screenshot after publishing release: Actions → `CD` run with green `Success`.

### B3) Registry image tag screenshot
- Screenshot: DockerHub/ECR showing newly published tag matching release version.

## Part C — End-to-End Evidence (Required)

### C1) Release page screenshot
- Screenshot: GitHub Release page for new version (e.g., `v0.3.0`).

### C2) Matching registry tag screenshot
- Screenshot: same version tag visible in DockerHub/ECR.

## Exact Step-by-Step: What to Screenshot

1. Open the repo in browser: https://github.com/nv23046/cc302-flask-to-do-app
2. Open [.github/workflows/ci.yml](.github/workflows/ci.yml) on GitHub and take screenshot #1 (CI file content).
3. Open [.github/workflows/cd.yml](.github/workflows/cd.yml) on GitHub and take screenshot #2 (CD file content).
4. Open CI failed run link: https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22542415824 and take screenshot #3 (red run + failing step).
5. Open CI success run link: https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22542450801 and take screenshot #4 (green run).
6. In GitHub repo, go to `Settings` → `Secrets and variables` → `Actions`; confirm `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` exist (do not show values), then take screenshot #5.
7. Go to `Releases` → `Draft a new release`, create tag `v0.3.0`, publish release.
8. Go to `Actions` tab, open `CD` workflow run for `v0.3.0`, wait for green success, take screenshot #6.
9. Open DockerHub repository tags page for your image and take screenshot #7 showing tag `0.3.0` (and `latest` if visible).
10. Open GitHub release page for `v0.3.0` and take screenshot #8.

## Secrets Verification (Required, no secret values)
- `DOCKERHUB_USERNAME` configured in GitHub repo secrets.
- `DOCKERHUB_TOKEN` configured in GitHub repo secrets.
- No secret values stored in repository files.

## Reflection (Ready to submit)
Using GitHub Actions helped me automate quality checks and deployment steps so I no longer rely on manual commands for every change. The CI workflow gave immediate feedback on lint and tests, which made it easier to catch issues before merging to main. The CD workflow connected releases to container publishing, so each release tag produced a matching Docker image tag automatically. I also learned the importance of GitHub Secrets for secure credentials and the difference between a failing and fixed pipeline run as evidence of troubleshooting. Overall, automation made my workflow faster, more reliable, and easier to reproduce.

## Final Marking Checklist
- [x] CI workflow file shown
- [x] CI green run screenshot link prepared
- [x] CI red run screenshot link prepared
- [x] CI fixed-green run available
- [x] CD workflow file shown
- [ ] CD green run screenshot
- [ ] Registry tag screenshot
- [ ] Release page screenshot
- [x] Reflection included
- [ ] Submitted PDF/Markdown
