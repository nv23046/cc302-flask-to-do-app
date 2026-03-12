# Branch Quality Gate Evidence Pack (Screenshot-Only)

## Student Info
- Student ID: nv23046
- Course: CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- PR Link (feature -> dev): https://github.com/nv23046/cc302-flask-to-do-app/pull/5

## Screenshot Checklist (Take Exactly These)
1. Branch rule for dev in GitHub Settings showing:
   - Require a pull request before merging = ON
   - Require status checks to pass before merging = ON
   - Required check includes test (CI - Build and Test)
2. PR #5 page showing merge blocked when CI is red with message equivalent to Required checks have not passed.
3. Failed CI run page for this PR (red):
   - https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22992427744
4. Same PR #5 page after fix showing CI green and merge allowed.
5. Passing CI run page for this PR (green):
   - https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22992478076
6. Branch rule for main showing the same two protections enabled:
   - Require pull request before merging = ON
   - Require status checks to pass before merging = ON

## 5-7 Line Explanation (Use This)
I created a feature branch and opened a pull request into dev.
To prove the quality gate, I introduced a controlled failure and CI turned red.
Because required checks were not passing, the PR merge was blocked.
I then fixed the failing issue and pushed to the same PR branch.
CI reran and turned green, and the PR became mergeable.
This confirms that branch protection and required status checks are working correctly.

## Zip Filename
CC302_WXX_nv23046_Evidence.zip
