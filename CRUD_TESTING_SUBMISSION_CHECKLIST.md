# CRUD Testing Assignment Submission Checklist

## Student / Repo

- Student ID: nv23046
- Course: CC312/CC302
- Repository: https://github.com/nv23046/cc312-flask-to-do-app
- Branch: main

## Required Files

- [x] tests/ folder exists
- [x] tests/test_crud.py created: [tests/test_crud.py](tests/test_crud.py)
- [x] pytest added to requirements.txt: [requirements.txt](requirements.txt)

## Test Coverage (Create, Update, Delete)

- [x] Create test implemented
- [x] Update test implemented
- [x] Delete test implemented
- [x] Read/verify step included (status + content/list validation)

## Evidence to Attach (Screenshots)

- [x] Passing run (green): [evidence/01_green_initial.txt](evidence/01_green_initial.txt)
- [x] One intentional failing run (red): [evidence/02_red_intentional_failure.txt](evidence/02_red_intentional_failure.txt)
- [x] Fixed run (green again): [evidence/03_green_after_fix.txt](evidence/03_green_after_fix.txt)

## Commands Used

- pip install -r requirements.txt
- pytest -q

## Test File

- [tests/test_crud.py](tests/test_crud.py)

## Reflection: What testing taught me about reliability

Automated CRUD tests made reliability measurable and repeatable. I learned that checking both HTTP status and visible list/content changes catches regressions faster than manual checks. Running one intentional failure also proved that tests quickly highlight breakage and guide confident fixes.

## Final Submission Pack

- [x] Repo link included
- [x] Passing evidence included
- [x] Failing evidence included
- [x] Fixed-after-fail evidence included
- [x] test_crud.py included/linked
- [x] Reflection paragraph included

## Optional (if your instructor strictly requires image screenshots)

- Convert each evidence text file into screenshot images before upload:
	- [evidence/01_green_initial.txt](evidence/01_green_initial.txt)
	- [evidence/02_red_intentional_failure.txt](evidence/02_red_intentional_failure.txt)
	- [evidence/03_green_after_fix.txt](evidence/03_green_after_fix.txt)
