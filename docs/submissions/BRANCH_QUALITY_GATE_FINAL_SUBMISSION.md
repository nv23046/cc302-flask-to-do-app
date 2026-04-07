# CC302 Branch Quality Gate Final Submission

## Student Information
- Student ID: nv23046
- Course: CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- Submission File Name: CC302_WXX_nv23046_Evidence.zip

---

## Branch List Evidence
```text
	dev                                  fc52983 [origin/dev] Merge pull request #3 from nv23046/feature/feat3
	feature/feat1                        0e5c23c [origin/feature/feat1] feat: add feature/feat1 change
	feature/feat2                        3bfc742 [origin/feature/feat2] feat: add feature/feat2 change
	feature/feat3                        c0372a2 [origin/feature/feat3] feat: add feature/feat3 change
	feature/filters-sorting              510c40c [origin/feature/filters-sorting] feat(filters): add advanced filtering and sorting capabilities
* feature/quality-gate-fail-pass-proof b990acc [origin/feature/quality-gate-fail-pass-proof] docs: add branch quality gate submission documents
	feature/task-descriptions            e82f270 [origin/feature/task-descriptions] feat(tasks): add description, priority, due_date, and status fields
	feature/task-tags                    c2ce9ed [origin/feature/task-tags] feat(tags): implement task tags and label management system
	main                                 4d78b1a [origin/main: behind 1] docs: add one-file final CI/CD submission template
```

---

## Pull Requests (Merged Workflow)
- Feature branch 1 → dev (feature/feat1): https://github.com/nv23046/cc302-flask-to-do-app/pull/1
- Feature branch 2 → dev (feature/feat2): https://github.com/nv23046/cc302-flask-to-do-app/pull/2
- Feature branch 3 → dev (feature/feat3): https://github.com/nv23046/cc302-flask-to-do-app/pull/3
- dev → main: https://github.com/nv23046/cc302-flask-to-do-app/pull/4
- Quality gate verification PR (branch protection enforcement): https://github.com/nv23046/cc302-flask-to-do-app/pull/5

*Note: PRs #1-#4 demonstrate the feature-branch workflow (feat1/2/3 → dev → main). PR #5 proves branch protection and required status checks are enforced (awaiting approval, CI required).*

---

## Branch Protection Rules (Screenshots)

### Screenshot 1: Dev & Main Protection Rules
URL: https://github.com/nv23046/cc302-flask-to-do-app/settings/branches

Evidence shows:
- Both `main` and `dev` branches have protection rules enabled
- Pull request review required before merge
- Required status checks enabled (CI pipeline must pass)

### Screenshot 2: CI Status Checks in PR #5
URL: https://github.com/nv23046/cc302-flask-to-do-app/pull/5 → Checks tab

Evidence shows:
- All CI checks passing (green checkmark)
- Status checks are required and validated
- PR cannot merge without these checks passing

### Screenshot 3: PR Merge Protection (Awaiting Approval)
URL: https://github.com/nv23046/cc302-flask-to-do-app/pull/5

Evidence shows:
- PR requires reviewer approval before merge
- Branch protection rule enforcement in action
- Even with passing CI, merge is blocked until approval

### Screenshot 4: DockerHub Registry Published
URL: https://hub.docker.com/r/nv23046/todo-saas

Evidence shows:
- Docker image successfully pushed to public registry
- Tags `0.1.0` and `latest` available
- Build metadata and image details visible

---

## Release And Versioning
- Git tag: v0.1.0
- GitHub Release: https://github.com/nv23046/cc302-flask-to-do-app/releases/tag/v0.1.0
- Release notes: Describe the three feature merges into dev, dev merge into main, and Docker image publication at version 0.1.0

---

## Docker Evidence
- Docker image: `nv23046/todo-saas:0.1.0`
- Docker registry: https://hub.docker.com/r/nv23046/todo-saas
- Built with: `docker build --build-arg VERSION=0.1.0 -t nv23046/todo-saas:0.1.0 .`
- Pushed to DockerHub with write-scoped credentials
- Tags published: `0.1.0` (semantic version) and `latest` (current release)

---

## Workflow Explanation

I created a dev branch from main and merged three feature branches into it through pull requests. Each feature branch (features/feat1, feat2, feat3) stayed focused on one logical change, keeping the commit history readable and enabling proper code review at each PR merge.

After the three feature branches were successfully merged into dev via their respective PRs, I merged the dev branch back into main via PR #4, ensuring the release branch only receives validated code from the integration branch.

I tagged this release as v0.1.0 using semantic versioning and built a Docker image with the same version number to maintain consistency between the code release and the containerized artifact.

The branch protection rules enforce that:
- All pull requests require at least one reviewer approval
- CI pipeline (GitHub Actions) must pass before any merge
- No direct pushes to main or dev without PR review

PR #5 demonstrates this quality gate in action: the PR shows CI checks are required and awaiting approval, proving the branch protection rules are actively enforced.

This complete workflow showcases integration testing (CI checks), code review requirements (PR approval), version management (semantic versioning), and artifact publication (Docker registry)—forming a professional CI/CD pipeline.
