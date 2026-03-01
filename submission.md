# Submission Checklist

## Branch list output

Attach `branches.txt` and `branches_log.txt` here or paste their contents.

## 3 PR links (feature → dev)

- PR 1: 
- PR 2: 
- PR 3: 

## 1 PR link (dev → main)

- Dev→Main PR: 

## DockerHub screenshot (tags visible)

Add an image showing the DockerHub repository **Tags** page.

## GitHub Release link

- Release: 

## Short paragraph: what I learned about branching + merging

Working with feature branches and a `dev` integration branch taught me that smaller, focused PRs make reviews and merges easier and reduce conflicts. Keeping `dev` updated frequently and merging only after review and basic checks helps keep the `main` branch stable and deployable. Using PRs for discussion and CI ensures quality and documents intent for future contributors.

---

Place screenshots and links above, then convert this file to PDF for submission.

---

# Assignment: CRUD Testing (pytest + Flask test client)

## Repo link

- https://github.com/nv23046/cc312-flask-to-do-app

## Required evidence (attach screenshots)

- Passing tests run (`pytest -q`) showing all CRUD tests green
- One intentional failing run (red)
- Fixed run after correction (green again)

## Test file

- tests/test_crud.py

## Reflection (Reliability)

Writing automated CRUD tests made reliability measurable instead of assumed. I learned that each change should be validated by behavior (status code + visible content/list changes), and test isolation with a separate database prevents flaky results. The intentional failing run also showed how quickly tests detect regressions and guide fast fixes.

## Quick submit checklist

- [ ] `tests/` folder exists
- [ ] `tests/test_crud.py` includes Create, Update, Delete tests
- [ ] At least one read/verify step is present in each test (page content/list check)
- [ ] `pytest` added in requirements and installed
- [ ] Green run screenshot captured
- [ ] Red run screenshot captured
- [ ] Green-after-fix screenshot captured
