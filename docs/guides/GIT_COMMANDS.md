# Git Workflow Quick Reference

## One-Time Setup (Initial)
```bash
# Create dev branch from main (run once)
git checkout main
git pull origin main
git checkout -b dev
git push -u origin dev
```

---

## Starting a New Feature
```bash
# Update dev branch
git checkout dev
git pull origin dev

# Create feature branch
git checkout -b feature/your-feature-name
git push -u origin feature/your-feature-name

# Work on feature (commit regularly)
git add .
git commit -m "feat(scope): description of change"
git push origin feature/your-feature-name
```

---

## Committing Code (While Working)
```bash
# Feature implementation
git commit -m "feat(auth): add email verification for signup"

# Bug fix
git commit -m "fix(ui): resolve button alignment on mobile"

# Performance improvement
git commit -m "perf(api): cache task queries in Redis"

# Documentation
git commit -m "docs(readme): add setup instructions"

# Code cleanup (no behavior change)
git commit -m "refactor(tasks): extract validation logic to helper"

# Test additions
git commit -m "test(auth): add unit tests for login flow"

# Push to remote
git push origin feature/your-feature-name
```

---

## Opening a Pull Request
```bash
# Push all commits first
git push origin feature/your-feature-name

# Open PR on GitHub (or use CLI)
gh pr create --base dev --head feature/your-feature-name \
  --title "feat: user authentication system" \
  --body "Implements login, logout, and session management"

# Check PR status
gh pr checks feature/your-feature-name
```

---

## Merging Feature into Dev
```bash
# Check out dev and update
git checkout dev
git pull origin dev

# Merge feature branch (preserves history)
git merge --no-ff feature/your-feature-name \
  -m "Merge branch 'feature/your-feature-name' into dev"

git push origin dev

# Delete feature branch (cleanup)
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

---

## Releasing to Production (Dev → Main)
```bash
# Update main
git checkout main
git pull origin main

# Merge dev into main
git merge --no-ff dev -m "Merge branch 'dev' into main for release v1.1.0"

# Tag the release
git tag -a v1.1.0 -m "Release v1.1.0 - Feature 1 and Feature 2"

# Push changes and tags
git push origin main --tags

# Sync dev with main
git checkout dev
git pull origin dev
git merge --no-ff main -m "Sync dev with main after release v1.1.0"
git push origin dev

# Build and push Docker image
VERSION="1.1.0"
docker build -t nv23046/cc312-flask-to-do-app:$VERSION \
  -t nv23046/cc312-flask-to-do-app:latest .
docker push nv23046/cc312-flask-to-do-app:$VERSION
docker push nv23046/cc312-flask-to-do-app:latest
```

---

## Fixing Production Bug (Hotfix)
```bash
# Create hotfix from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-bug
git push -u origin hotfix/critical-bug

# Fix the bug and commit
git commit -m "fix(security): sanitize user input"

# Merge to main
git checkout main
git merge --no-ff hotfix/critical-bug -m "Merge critical fix"
git tag -a v1.0.1 -m "Hotfix v1.0.1"
git push origin main --tags

# Merge to dev
git checkout dev
git merge --no-ff hotfix/critical-bug -m "Merge hotfix into dev"
git push origin dev

# Cleanup
git branch -d hotfix/critical-bug
git push origin --delete hotfix/critical-bug

# Release Docker image
docker build -t nv23046/cc312-flask-to-do-app:1.0.1 -t nv23046/cc312-flask-to-do-app:latest .
docker push nv23046/cc312-flask-to-do-app:1.0.1
docker push nv23046/cc312-flask-to-do-app:latest
```

---

## Common Tasks

### View Git History
```bash
git log --graph --oneline --all
# Output:
# * abc1234 (HEAD -> main, tag: v1.2.0) Merge branch 'dev' into main
# *   def5678 (dev) Merge branch 'feature/tasks' into dev
# |\ 
# | * xyz9999 (feature/tasks) feat(tasks): add priority system
# |/
# * aaa0000 Release v1.1.0
```

### Check Current Branch Status
```bash
git status
git branch -a
git log --oneline -n 5
```

### Undo Last Commit (Not Yet Pushed)
```bash
# Keep changes
git reset --soft HEAD~1

# Discard changes
git reset --hard HEAD~1
```

### Sync Feature Branch with Dev (If Dev Updated)
```bash
git checkout feature/your-feature
git fetch origin
git rebase origin/dev
# OR
git merge origin/dev
git push origin feature/your-feature
```

### Delete Local and Remote Branch
```bash
git branch -d feature/your-feature
git push origin --delete feature/your-feature
```

### List All Tags
```bash
git tag -l
git tag -l "v1.*"  # Filter by pattern
```

### Create Release Notes
```bash
# Show changes between tags
git log v1.0.0..v1.1.0 --oneline

# Pretty format for release notes
git log v1.0.0..v1.1.0 --pretty=format:"%h - %s (%an)" | sort
```

---

## Conventional Commit Reference

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **perf**: Performance improvement
- **refactor**: Code reorganization (no behavior change)
- **test**: Adding/updating tests
- **docs**: Documentation updates
- **chore**: Maintenance (dependencies, build, etc.)
- **ci**: CI/CD configuration changes

### Scope (Optional but Recommended)
- auth, tasks, ui, api, database, docker, etc.

### Subject Guidelines
- Imperative mood ("add" not "adds" or "added")
- No capital letter at start
- No period at end
- 50 characters or less

---

## Version Numbering Quick Reference

| Change | Old Version | New Version | Example |
|--------|-------------|-------------|---------|
| Bug fix | 1.0.0 | 1.0.1 | XSS vulnerability fix |
| New feature | 1.0.0 | 1.1.0 | Add task categories |
| Breaking change | 1.0.0 | 2.0.0 | Add user authentication |

---

## Safety Checklist Before Release

- [ ] All feature branches merged to dev
- [ ] Tests passing on dev
- [ ] No uncommitted changes
- [ ] dev branch up to date with origin
- [ ] Version number decided (MAJOR, MINOR, PATCH)
- [ ] CHANGELOG.md updated
- [ ] Git tag created with semantic version
- [ ] Docker image built and tested
- [ ] Docker image tagged with version
- [ ] All tags pushed to GitHub
- [ ] Docker image pushed to registry
