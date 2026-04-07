# CC302 Branch Quality Gate Final Submission

## Student Information
- Student ID: nv23046
- Course: CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- Submission File Name: CC302_WXX_nv23046_Evidence.zip

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

## Pull Requests
- Feature branch 1 -> dev: https://github.com/nv23046/cc302-flask-to-do-app/pull/1
- Feature branch 2 -> dev: https://github.com/nv23046/cc302-flask-to-do-app/pull/2
- Feature branch 3 -> dev: https://github.com/nv23046/cc302-flask-to-do-app/pull/3
- dev -> main: https://github.com/nv23046/cc302-flask-to-do-app/pull/4

## Release And Versioning
- Git tag: v0.1.0
- GitHub Release: https://github.com/nv23046/cc302-flask-to-do-app/releases/tag/v0.1.0
- Release notes already describe the three feature merges and the published Docker image version 0.1.0.

## Docker Evidence
- Local image build succeeded with: `docker build --build-arg VERSION=0.1.0 -t nv23046/todo-saas:0.1.0 .`
- Local image tag exists as `nv23046/todo-saas:0.1.0`.
- A push attempt from this environment failed because the available DockerHub token does not have write scope, so the registry publish step still needs a write-scoped DockerHub credential.

## Short Explanation
I created a dev branch from main and merged three feature branches into it through pull requests.
Each feature branch stayed focused on one change set, which kept the history readable and easier to review.
After the feature merges, I merged dev back into main so the release branch stayed stable.
I tagged the release as v0.1.0 and used that semantic version for the Docker image build.
This workflow showed how branch protection, PR reviews, and versioned releases fit together cleanly.
