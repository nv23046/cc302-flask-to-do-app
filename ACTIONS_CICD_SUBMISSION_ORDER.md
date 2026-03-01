# GitHub Actions CI/CD — Submission Order (Paste Screenshots Here)

## Student Info
- Student ID: nv23046
- Course: CC312/CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- Branch: main

## 1) CI Workflow File
- File link: [.github/workflows/ci.yml](.github/workflows/ci.yml)
- Screenshot to insert below:

![CI workflow file](images/01-ci-workflow-file.png)

## 2) CD Workflow File
- File link: [.github/workflows/cd.yml](.github/workflows/cd.yml)
- Screenshot to insert below:

![CD workflow file](images/02-cd-workflow-file.png)

## 3) Failed CI Run (Red)
- Run link: https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22542415824
- Screenshot to insert below:

![CI failed run](images/03-ci-failed-red.png)

## 4) Fixed CI Run (Green)
- Run link: https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22542450801
- Screenshot to insert below:

![CI fixed green run](images/04-ci-fixed-green.png)

## 5) Secrets Configured (Names only, no values)
- Page: Repo Settings → Secrets and variables → Actions
- Must show: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`
- Screenshot to insert below:

![GitHub secrets configured](images/05-secrets-names-only.png)

## 6) Successful CD Run (Green)
- Trigger by publishing release (e.g., `v0.3.0`)
- Screenshot to insert below:

![CD successful run](images/06-cd-green-run.png)

## 7) Registry Tag Screenshot (DockerHub/ECR)
- Must show version tag matching release (e.g., `0.3.0`)
- Screenshot to insert below:

![Registry image tag](images/07-registry-tag.png)

## 8) GitHub Release Page
- Must show published release (e.g., `v0.3.0`)
- Screenshot to insert below:

![GitHub release page](images/08-github-release.png)

## Reflection (Paste as-is)
Using GitHub Actions helped me automate quality checks and deployment steps so I no longer rely on manual commands for every change. The CI workflow gave immediate feedback on lint and tests, which made it easier to catch issues before merging to main. The CD workflow connected releases to container publishing, so each release tag produced a matching Docker image tag automatically. I also learned the importance of GitHub Secrets for secure credentials and the difference between a failing and fixed pipeline run as evidence of troubleshooting. Overall, automation made my workflow faster, more reliable, and easier to reproduce.

## Final Check Before Submit
- [ ] All 8 screenshots inserted
- [ ] Image paths updated if needed
- [ ] Links open correctly
- [ ] Reflection present
- [ ] Exported to PDF (if required)
- [ ] Submitted
