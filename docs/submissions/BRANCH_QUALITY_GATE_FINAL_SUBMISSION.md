# CC302 Branch Quality Gate Final Submission

## Student Information
- Student ID: nv23046
- Course: CC302
- Repository: https://github.com/nv23046/cc302-flask-to-do-app
- PR Link (feature -> dev): https://github.com/nv23046/cc302-flask-to-do-app/pull/5
- Submission File Name: CC302_WXX_nv23046_Evidence.zip

## Screenshot 1 - Dev Branch Protection Rule
Paste screenshot here.

Required to show:
- Require a pull request before merging = ON
- Require status checks to pass before merging = ON
- Required check includes: test (CI - Build and Test)

## Screenshot 2 - PR Blocked (Red Gate)
Paste screenshot here.

Open:
- https://github.com/nv23046/cc302-flask-to-do-app/pull/5

Required to show:
- Merge blocked state
- Message equivalent to: Required checks have not passed

## Screenshot 3 - Failed CI Run (Red)
Paste screenshot here.

Open:
- https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22992427744

Required to show:
- Workflow run is failed (red)
- Workflow name visible

## Screenshot 4 - PR Allowed (Green Gate)
Paste screenshot here.

Open:
- https://github.com/nv23046/cc302-flask-to-do-app/pull/5

Required to show:
- Checks are green
- Merge is allowed

## Screenshot 5 - Passing CI Run (Green)
Paste screenshot here.

Open:
- https://github.com/nv23046/cc302-flask-to-do-app/actions/runs/22992478076

Required to show:
- Workflow run is successful (green)
- Workflow name visible

## Screenshot 6 - Main Branch Protection Rule
Paste screenshot here.

Required to show:
- Require a pull request before merging = ON
- Require status checks to pass before merging = ON

## Short Explanation (5-7 lines)
I created a feature branch and opened a pull request into dev.
To prove the quality gate, I introduced a controlled failure and CI turned red.
Because required checks were not passing, the PR merge was blocked.
I then fixed the failing issue and pushed to the same PR branch.
CI reran and turned green, and the PR became mergeable.
This confirms that branch protection and required status checks are working correctly.

## Final Check Before Submission
- All 6 screenshots pasted
- PR link present
- Explanation included
- Zip file named exactly: CC302_WXX_nv23046_Evidence.zip
