# Professional Git Branching & Docker Versioning Strategy

## 1. Git Branching Strategy (Gitflow-Inspired)

### Branch Hierarchy
```
main (production, protected)
  └─ tagged releases (v1.0.0, v1.1.0, etc.)
  
dev (integration, protected)
  └─ feature/* (temporary, auto-deleted after merge)
```

### Branch Protection Rules (Set in GitHub)
- **main**: Require PR reviews, enforce branch is up to date, dismiss stale reviews
- **dev**: Require at least 1 approval, allow self-approvals for testing

---

## 2. Exact Git Commands by Workflow

### Initial Setup: Create Dev Branch from Main
```bash
# Ensure you're on main and it's up to date
git checkout main
git pull origin main

# Create dev branch from main (one-time setup)
git checkout -b dev
git push -u origin dev

# Configure branch protection in GitHub (UI or CLI)
gh api repos/nv23046/cc312-flask-to-do-app/branches/dev/protection \
  --input - << 'EOF'
{
  "enforce_admins": true,
  "required_status_checks": null,
  "required_pull_request_reviews": {"dismiss_stale_reviews": true}
}
EOF
```

### Creating Feature Branches
```bash
# Always start from updated dev
git checkout dev
git pull origin dev

# Create feature branch with conventional naming
git checkout -b feature/user-authentication
# or: feature/api-endpoints, feature/dark-mode, etc.

# Push to remote with tracking
git push -u origin feature/user-authentication
```

### Committing with Conventional Commits
```bash
# Format: type(scope): description

# Feature additions
git commit -m "feat(auth): implement user login with email verification"
git commit -m "feat(tasks): add task priority levels"

# Bug fixes
git commit -m "fix(ui): resolve responsive design issue on mobile"

# Performance improvements
git commit -m "perf(database): optimize task query with indexing"

# Documentation
git commit -m "docs(readme): update installation instructions"

# Code refactoring (no functional change)
git commit -m "refactor(validation): extract password rules into constants"

# Push commits
git push origin feature/user-authentication
```

### Merging Feature → Dev (Via Pull Request)
```bash
# Step 1: Open PR on GitHub UI
# Title: "feat: add user authentication system"
# Description should include:
#   - What problem does this solve?
#   - What are the changes?
#   - Any breaking changes? (important for versioning)

# Step 2: After approval, merge via CLI (if not using GitHub merge button)
git checkout dev
git pull origin dev
git merge --no-ff feature/user-authentication -m "Merge branch 'feature/user-authentication' into dev"
git push origin dev

# Step 3: Delete feature branch (cleanup)
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication
```

### Merging Dev → Main (Release Process)
```bash
# Step 1: Ensure dev is ready for production
git checkout dev
git pull origin dev

# Step 2: Verify all tests pass, build succeeds
# (This should be automated in CI/CD)

# Step 3: Create release branch (optional but recommended)
git checkout -b release/v1.2.0
# OR skip release branch for simple projects and go straight to merge

# Step 4a: Merge release/dev to main
git checkout main
git pull origin main
git merge --no-ff dev -m "Merge branch 'dev' into main for release v1.2.0"

# Step 4b: Tag the release
git tag -a v1.2.0 -m "Release version 1.2.0 - UserAuth and Task Priority features"
git push origin main --tags

# Step 5: Merge main back to dev to sync
git checkout dev
git pull origin dev
git merge --no-ff main -m "Sync dev with main after release v1.2.0"
git push origin dev

# Step 6: Delete release branch if used
git branch -d release/v1.2.0
git push origin --delete release/v1.2.0
```

### Handling Hotfixes (Critical Production Bugs)
```bash
# Create hotfix branch directly from main
git checkout main
git pull origin main
git checkout -b hotfix/security-patch

# Make fix, commit with conventional commit
git commit -m "fix(security): sanitize user input to prevent XSS attacks"

# Merge to main (bump PATCH version)
git checkout main
git merge --no-ff hotfix/security-patch -m "Merge hotfix: security patch"
git tag -a v1.2.1 -m "Security patch - XSS vulnerability"
git push origin main --tags

# Merge hotfix back to dev
git checkout dev
git merge --no-ff hotfix/security-patch -m "Merge hotfix into dev"
git push origin dev

# Cleanup
git branch -d hotfix/security-patch
git push origin --delete hotfix/security-patch
```

---

## 3. Six Realistic Feature Branches for To-Do App

### Feature 1: User Authentication System
- **Branch**: `feature/user-authentication`
- **Description**: Implement user login/logout, registration, session management with email verification
- **Version Bump**: **MAJOR** (v1.0.0 → v2.0.0)
- **Why**: Fundamental change in app architecture (stateless → stateful with users); breaking API changes; database schema changes for user table

### Feature 2: Task Prioritization System
- **Branch**: `feature/task-priorities`
- **Description**: Add priority levels (High/Medium/Low) to tasks, filter/sort by priority, visual indicators in UI
- **Version Bump**: **MINOR** (v1.0.0 → v1.1.0)
- **Why**: New functionality that doesn't break existing features; existing tasks work without priority (optional field); additive API changes

### Feature 3: Dark Mode Theme
- **Branch**: `feature/dark-mode-ui`
- **Description**: Add light/dark theme toggle, persist user preference in localStorage, update all templates with theme-aware CSS
- **Version Bump**: **PATCH** (v1.0.0 → v1.0.1)
- **Why**: UI-only enhancement; no API changes; no data model changes; completely backward compatible

### Feature 4: Task Categories/Tags
- **Branch**: `feature/task-categories`
- **Description**: Add category/tag system, organize tasks by category, filter tasks by category, update UI with category chips
- **Version Bump**: **MINOR** (v1.0.0 → v1.1.0)
- **Why**: New data model (categories table) and API endpoints for managing categories; existing tasks work without categories; additive changes

### Feature 5: Due Date Notifications
- **Branch**: `feature/deadline-notifications`
- **Description**: Add due date field to tasks, background job to check overdue tasks, send notifications/reminders via email or UI alerts
- **Version Bump**: **MINOR** (v1.0.0 → v1.1.0)
- **Why**: New background task system and API endpoints; existing tasks optional; doesn't break current workflow; new feature addition

### Feature 6: API Rate Limiting & Analytics
- **Branch**: `feature/api-rate-limiting`
- **Description**: Implement rate limiting per user/IP, add analytics tracking for API endpoints, Dashboard with usage metrics
- **Version Bump**: **PATCH** (v1.0.0 → v1.0.1)
- **Why**: Infrastructure/operational improvement; tracking is transparent to users; no API contract changes; existing endpoints work as before

---

## 4. Docker Versioning Rules

### Semantic Versioning for Docker Images
```
MAJOR.MINOR.PATCH
Example: nv23046/cc312-flask-to-do-app:2.1.3
```

### When to Increment Each Component

| Version Type | Increment When | Example |
|---|---|---|
| **MAJOR** | Breaking changes to app architecture, data model, authentication, or API contracts | User auth system added (stateless → stateful); Database schema requires migration; API endpoint signature changed |
| **MINOR** | New features that are backward compatible; new API endpoints; new data fields (optional) | Task priorities added; Categories system added; Asset upload feature added |
| **PATCH** | Bug fixes; UI tweaks; performance improvements; security patches; documentation updates | Fixed task deletion race condition; Dark mode CSS fix; Updated dependencies for security; Optimized database query |

### Example Docker Build & Push Commands

#### Build with Version Tags
```bash
# Set version
export VERSION="1.0.0"

# Build image with multiple tags
docker build \
  -t nv23046/cc312-flask-to-do-app:$VERSION \
  -t nv23046/cc312-flask-to-do-app:latest \
  .

# Or with detailed tags
docker build \
  -t nv23046/cc312-flask-to-do-app:1.0.0 \
  -t nv23046/cc312-flask-to-do-app:1.0 \
  -t nv23046/cc312-flask-to-do-app:latest \
  .
```

#### Push to Docker Hub
```bash
# Push specific version
docker push nv23046/cc312-flask-to-do-app:1.0.0

# Push latest
docker push nv23046/cc312-flask-to-do-app:latest

# Push all tags
docker push nv23046/cc312-flask-to-do-app --all-tags
```

#### Complete Release Workflow with Docker
```bash
# 1. Merge dev to main and tag
git checkout main
git pull origin main
git merge --no-ff dev -m "Release v1.1.0"
git tag -a v1.1.0 -m "v1.1.0 - Task Priorities and Categories"
git push origin main --tags

# 2. Build Docker image from source
export VERSION="1.1.0"
docker build -t nv23046/cc312-flask-to-do-app:$VERSION \
  -t nv23046/cc312-flask-to-do-app:latest \
  .

# 3. Push to registry
docker push nv23046/cc312-flask-to-do-app:$VERSION
docker push nv23046/cc312-flask-to-do-app:latest

# 4. (Optional) Tag for patch releases
docker build -t nv23046/cc312-flask-to-do-app:1.1 .
docker push nv23046/cc312-flask-to-do-app:1.1

# 5. Sync dev with main
git checkout dev
git pull origin dev
git merge --no-ff main -m "Sync dev with main after v1.1.0 release"
git push origin dev
```

#### Automated Version Management (CI/CD)
```yaml
# Example GitHub Actions snippet for automated versioning
name: Release-Docker-Image
on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Extract version
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
      
      - name: Build and push
        run: |
          docker build -t nv23046/cc312-flask-to-do-app:${{ steps.version.outputs.VERSION }} \
            -t nv23046/cc312-flask-to-do-app:latest .
          docker push nv23046/cc312-flask-to-do-app:${{ steps.version.outputs.VERSION }}
          docker push nv23046/cc312-flask-to-do-app:latest
```

---

## 5. Real-World DevOps & CI/CD Practices Reflected

### Process & Traceability
- **Linear History**: `--no-ff` flag preserves merge commits, creating clear branch history readable in `git log --graph --oneline --all`
- **Conventional Commits**: Enables automated changelog generation and semantic versioning detection via tools like `commitizen` or `semantic-release`
- **Protected Branches**: Prevent accidental pushes to production; enforce code review discipline
- **Tagging**: Immutable release references; enables rollback to specific versions; links to deployment records

### Safe Delivery
- **Feature Isolation**: Each feature in separate branch; failures contained; easy rollback
- **Integration Testing**: Dev branch serves as integration point; catches conflicts early before production
- **Release Branch**: Optional but buffers production from active development; allows final QA before merge
- **Hotfix Path**: Critical fixes bypass dev; merged to both main and dev to prevent regression

### Semantic Versioning + Docker
- **Version Predictability**: Consumers of your image know breaking changes only on MAJOR bumps
- **Multi-tag Strategy**: Allows pinning to `1.1.3` (exact), `1.1` (patch updates), or `latest` (cutting edge)
- **Audit Trail**: Docker image tag = Git tag = Release notes; links code to deployed artifact

### Real-World Alignment
This workflow matches practices at companies like Netflix, GitHub, Google:
- Netflix: Uses semantic versioning for all deployments
- GitHub: Protected branches are mandatory for production repositories
- Google: Enforces conventional commits for changelog automation
- Instagram/Meta: Feature flags deployed through develop branch before main release

### Operations Benefits
- **Rollback**: `docker pull nv23046/cc312-flask-to-do-app:1.0.0` restores previous version instantly
- **Parallel Development**: Multiple teams work on different features without blocking
- **Release Cadence**: Can do releases daily, weekly, or on-demand without process overhead
- **Compliance**: Git history provides audit trail for regulatory requirements (HIPAA, SOC2, etc.)

---

## 6. Quick Reference Checklist

### Before Creating Feature Branch
- [ ] `git checkout dev && git pull origin dev`
- [ ] Understand if this is MAJOR/MINOR/PATCH scope
- [ ] Check existing issues/PRs to avoid duplication

### While Developing
- [ ] Follow conventional commit format
- [ ] Create PR with clear description
- [ ] Include testing results
- [ ] Request review from team member

### Before Merging to Dev
- [ ] All tests passing
- [ ] Code reviewed and approved
- [ ] No merge conflicts
- [ ] Updated relevant documentation

### Before Merging Dev to Main (Release)
- [ ] All features on dev are ready for production
- [ ] No open PRs on dev
- [ ] Version in `requirements.txt` or `app.py` reflects new version (optional but recommended)
- [ ] CHANGELOG.md updated with features/fixes
- [ ] Tested against staging environment

### After Releasing
- [ ] Tag created: `git tag -a vX.Y.Z`
- [ ] Docker image built and pushed with matching tag
- [ ] Dev branch synced back with main
- [ ] Release notes published on GitHub
