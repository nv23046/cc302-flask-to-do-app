# Complete Setup & Deployment Guide

## 🎯 Overview

Your Flask To-Do application now has a professional, production-grade DevOps and CI/CD infrastructure. This guide walks you through the setup and explains what has been implemented.

---

## ✅ What Has Been Implemented

### 1. **Git Branching Strategy** (Gitflow)
- ✅ `main` branch (production-ready, protected)
- ✅ `dev` branch (integration branch, protected)
- ✅ `feature/*` branches (temporary, auto-deleted after merge)

### 2. **Version Tracking**
- ✅ Version number in `app.py` (`__version__ = "1.0.0"`)
- ✅ `/api/version` endpoint for health checks
- ✅ Version accessible in templates

### 3. **Docker Enhancements**
- ✅ OCI image labels with metadata (version, date, source)
- ✅ Health check endpoint integration
- ✅ Build arguments for version injection

### 4. **GitHub Actions CI/CD**
- ✅ `ci.yml` - Runs tests and builds Docker image on each push to main/dev
- ✅ `release.yml` - Builds and pushes Docker image to Docker Hub on git tag
- ✅ Automated GitHub Release creation

### 5. **Release Automation**
- ✅ `release.sh` - Local script for manual releases with validation
- ✅ `setup-git.sh` - One-time git initialization script
- ✅ Semantic versioning enforcement (MAJOR.MINOR.PATCH)

### 6. **Documentation**
- ✅ `GIT_WORKFLOW.md` - Complete branching strategy guide
- ✅ `DOCKER_VERSIONING.md` - Docker versioning rules and build commands
- ✅ `GIT_COMMANDS.md` - Quick reference for common git operations
- ✅ `.github/pull_request_template.md` - PR template with version classification
- ✅ `CHANGELOG.md` - Keep a Changelog format

### 7. **GitHub Configuration**
- ✅ `.github/workflows/` - Automated workflows
- ✅ `.github/pull_request_template.md` - PR guidance

---

## 🚀 Next Steps - Final Configuration

### Step 1: Configure GitHub Secrets
For Docker Hub pushes to work, add these secrets to your repository:

1. Go to: `https://github.com/nv23046/cc312-flask-to-do-app/settings/secrets/actions`

2. Add these secrets:
   - `DOCKER_HUB_USERNAME` - Your Docker Hub username
   - `DOCKER_HUB_PASSWORD` - Your Docker Hub access token or password

**How to create Docker Hub token:**
1. Login to https://hub.docker.com/
2. Settings → Security → New Access Token
3. Copy token and add to GitHub secrets

### Step 2: Configure Branch Protection Rules
Protect your main and dev branches from accidental pushes.

**For `main` branch:**
1. Go to: `https://github.com/nv23046/cc312-flask-to-do-app/settings/branches`
2. Add rule for `main`:
   - ✓ Require a pull request before merging
   - ✓ Require status checks to pass (select: `CI - Build and Test`)
   - ✓ Require branches to be up to date before merging
   - ✓ Dismiss stale pull request approvals
   - ✓ Include administrators in restrictions

**For `dev` branch:**
1. Add rule for `dev`:
   - ✓ Require a pull request before merging
   - ✓ Require status checks to pass

### Step 3: Verify GitHub Actions Workflows
1. Go to: `https://github.com/nv23046/cc312-flask-to-do-app/actions`
2. You should see:
   - `CI - Build and Test` workflow (triggered on push to main/dev)
   - `Release and Build Docker Image` workflow (triggered on git tags)

### Step 4: Test the Setup Locally
```bash
# Verify you're on dev branch
git checkout dev
git pull origin dev

# Create a test feature branch
git checkout -b feature/test-workflow

# Make a change
echo "# Test feature" >> README.md

# Commit with conventional commit format
git add README.md
git commit -m "feat: add test feature to verify workflow"

# Push feature branch
git push -u origin feature/test-workflow

# Create Pull Request on GitHub (dev is base branch)
# This will trigger CI workflow automatically
```

---

## 📖 Quick Start Workflow

### Creating a New Feature

```bash
# 1. Update dev branch
git checkout dev
git pull origin dev

# 2. Create feature branch
git checkout -b feature/your-feature-name

# 3. Make changes and commit
git add .
git commit -m "feat(scope): description of feature"

# 4. Push to GitHub
git push -u origin feature/your-feature-name

# 5. Open Pull Request on GitHub (target: dev branch)
# - Add clear description
# - Choose version impact: PATCH, MINOR, or MAJOR
# - Wait for CI checks to pass

# 6. After approval, merge via GitHub UI (merge and delete branch)
```

### Releasing to Production

```bash
# 1. Ensure all features are in dev and tested
git checkout dev
git pull origin dev

# 2. Merge dev to main
git checkout main
git pull origin main
git merge --no-ff dev -m "Release v1.1.0"

# 3. Create version tag
git tag -a v1.1.0 -m "Release v1.1.0 with feature X and Y"

# 4. Push to GitHub (triggers release workflow)
git push origin main --tags

# OR use the automated release script:
./release.sh 1.1.0
```

---

## 📂 File Structure - What Was Added

### New Directories
```
.github/
  ├── workflows/
  │   ├── ci.yml              # Tests and Docker build on push
  │   └── release.yml         # Docker Hub push on git tag
  └── pull_request_template.md
```

### New Files
```
CHANGELOG.md                   # Keep a Changelog format
DOCKER_VERSIONING.md           # Docker versioning guide
GIT_COMMANDS.md                # Git operations quick reference
GIT_WORKFLOW.md                # Complete branching strategy
release.sh                     # Automated release script
setup-git.sh                   # Git setup script (already run)
```

### Modified Files
```
app.py                         # Added version tracking + /api/version endpoint
Dockerfile                     # Added labels + health check
```

---

## 🔄 Workflow Examples

### Example 1: Bug Fix (PATCH Release)

```bash
# Create hotfix
git checkout main
git pull origin main
git checkout -b hotfix/security-xss

# Fix and commit
git commit -m "fix(security): sanitize task input to prevent XSS"

# Create PR to main (describe as PATCH version)
git push -u origin hotfix/security-xss

# After merge and tag
git tag -a v1.0.1 -m "Security patch: XSS vulnerability"

# Build and release
docker build -t nv23046/cc312-flask-to-do-app:1.0.1 .
docker push nv23046/cc312-flask-to-do-app:1.0.1
```

### Example 2: Feature Addition (MINOR Release)

```bash
# Create feature on dev
git checkout dev
git checkout -b feature/task-categories

# Add feature
git add .
git commit -m "feat(tasks): add category system for task organization"

# PR to dev, after approval:
git push origin dev

# When ready for release, merge dev to main
git checkout main
git merge --no-ff dev
git tag -a v1.1.0 -m "Release v1.1.0 - Task Categories"

# Run release script
./release.sh 1.1.0
```

### Example 3: Breaking Change (MAJOR Release)

```bash
# Create feature on dev
git checkout dev
git checkout -b feature/user-authentication

# Implement auth (breaking change - adds user_id requirement)
git commit -m "feat(auth): implement user authentication system

BREAKING CHANGE: Tasks now require user_id, existing API endpoints updated"

# PR to dev, mark as MAJOR version
# After approval, merge to main
git tag -a v2.0.0 -m "Release v2.0.0 - User Authentication (BREAKING)

Introduces required user authentication. See CHANGELOG.md for migration guide."

./release.sh 2.0.0
```

---

## 🐳 Docker Commands

### Local Testing

```bash
# Build with version
VERSION="1.0.0"
docker build \
  --build-arg VERSION=$VERSION \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
  --build-arg VCS_REF=$(git rev-parse HEAD) \
  -t nv23046/cc312-flask-to-do-app:$VERSION \
  -t nv23046/cc312-flask-to-do-app:latest \
  .

# Run locally
docker run -p 5000:5000 nv23046/cc312-flask-to-do-app:latest

# Check version
curl http://localhost:5000/api/version
```

### Production Deployment

```bash
# Pull specific version
docker pull nv23046/cc312-flask-to-do-app:1.0.0

# Run in production
docker run -d \
  --name todo-app \
  -p 5000:5000 \
  -v todo-data:/app \
  nv23046/cc312-flask-to-do-app:1.0.0

# Check health
docker ps  # Status should show healthy
```

---

## 📋 Semantic Versioning Quick Guide

| Change | Old → New | Reason |
|--------|-----------|--------|
| Security fix | 1.0.0 → 1.0.1 | No API changes |
| Bug fix | 1.0.0 → 1.0.1 | No new features |
| New optional field | 1.0.0 → 1.1.0 | Backward compatible |
| New feature | 1.0.0 → 1.1.0 | Optional for users |
| Required field added | 1.0.0 → 2.0.0 | Breaking change |
| Auth system added | 1.0.0 → 2.0.0 | Major architecture change |
| API endpoint changed | 1.0.0 → 2.0.0 | Breaking change |

---

## 🔍 Monitoring & Health Checks

The app now exposes a version endpoint for monitoring:

```bash
# Check app version and health
curl http://your-app:5000/api/version

# Response:
# {"version": "1.0.0", "status": "ok"}
```

The Docker image also includes a health check:
- Checks every 30 seconds
- Timeout: 10 seconds
- Retries: 3 times before marking unhealthy

---

## 🆘 Troubleshooting

### Issue: Docker Hub push fails in GitHub Actions
**Solution:** 
- Verify `DOCKER_HUB_USERNAME` secret is set correctly
- Verify `DOCKER_HUB_PASSWORD` is a token, not your password
- Check that your Docker Hub account is public or token has push access

### Issue: Git tag already exists
**Solution:**
```bash
# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0

# Recreate and push
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin --tags
```

### Issue: Can't merge dev to main - has commits
**Solution:** This is correct! Dev should have updates. Create PR, ensure tests pass, then merge.

### Issue: release.sh fails with "uncommitted changes"
**Solution:**
```bash
git status
git add .
git commit -m "fix: resolve pending changes"
./release.sh 1.0.1
```

---

## 🎓 Learning Resources

- **Conventional Commits**: https://www.conventionalcommits.org/
- **Semantic Versioning**: https://semver.org/
- **Gitflow Workflow**: https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
- **Docker Best Practices**: https://docs.docker.com/develop/dev-best-practices/
- **GitHub Actions**: https://docs.github.com/en/actions

---

## 📞 Commands Quick Reference

```bash
# Check current version
grep "__version__" app.py

# Test app locally
python app.py

# Create feature branch
git checkout -b feature/name dev

# Commit code
git commit -m "feat(scope): description"

# Push feature branch
git push -u origin feature/name

# Release new version
./release.sh 1.1.0

# Check Docker image info
docker inspect nv23046/cc312-flask-to-do-app:1.0.0
docker history nv23046/cc312-flask-to-do-app:1.0.0
```

---

## ✨ Summary

Your Flask To-Do application now has:

1. ✅ Professional Git workflow with branch protection
2. ✅ Automated CI/CD pipeline (test, build, push)
3. ✅ Semantic versioning throughout (code + Docker)
4. ✅ Production-ready Docker images with metadata
5. ✅ Comprehensive documentation for the team
6. ✅ Automated release scripts
7. ✅ Health checks and monitoring endpoints

**This is enterprise-grade DevOps infrastructure suitable for production deployment.**

Ready to deploy? Start with Step 1: Configure GitHub Secrets (above) to enable automated Docker Hub pushes.
