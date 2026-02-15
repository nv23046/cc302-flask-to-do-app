# Docker Versioning & Release Automation Guide

## Quick Docker Build & Release Process

### Standard Release Workflow
```bash
#!/bin/bash
# release.sh - Automate docker build and push with versioning

set -e

VERSION=$1
DOCKER_REGISTRY="nv23046"
DOCKER_IMAGE="cc312-flask-to-do-app"

if [ -z "$VERSION" ]; then
    echo "Usage: ./release.sh 1.2.3"
    exit 1
fi

echo "Building Docker image for version $VERSION..."
docker build \
    -t $DOCKER_REGISTRY/$DOCKER_IMAGE:$VERSION \
    -t $DOCKER_REGISTRY/$DOCKER_IMAGE:latest \
    .

echo "Pushing to Docker Hub..."
docker push $DOCKER_REGISTRY/$DOCKER_IMAGE:$VERSION
docker push $DOCKER_REGISTRY/$DOCKER_IMAGE:latest

echo "✓ Release $VERSION published to Docker Hub"
echo "  - Full: $DOCKER_REGISTRY/$DOCKER_IMAGE:$VERSION"
echo "  - Latest: $DOCKER_REGISTRY/$DOCKER_IMAGE:latest"
```

### Pre-Release Versioning Strategy

#### Determining the Next Version
```bash
# Get current version from latest tag
CURRENT=$(git describe --tags --abbrev=0 2>/dev/null || echo "0.0.0")
echo "Current version: $CURRENT"

# Increment for next release based on feature scope
# For MAJOR: v1.0.0 → v2.0.0
# For MINOR: v1.0.0 → v1.1.0
# For PATCH: v1.0.0 → v1.0.1

# Example with semantic-release (optional tool)
npm install --save-dev semantic-release
npx semantic-release --dry-run  # Shows what version would be released
```

#### Manual Version Management
```bash
# Create version file for reference
echo "1.2.0" > VERSION
git add VERSION
git commit -m "chore: bump version to 1.2.0"
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin main --tags

# Read version for docker build
VERSION=$(cat VERSION)
docker build -t nv23046/cc312-flask-to-do-app:$VERSION .
```

---

## Version Increment Decision Matrix

### When to Use MAJOR (Breaking Change)
```
Scenario: Switching from file-based storage to PostgreSQL database
- Old clients cannot work with new API structure
- Database schema incompatible with previous versions
- Config file format changed

Action: Bump from 1.x.x → 2.0.0
```

```
Scenario: User authentication system added
- App changed from public → user-based access
- API routes require authentication token now
- Data structure has user_id relationships

Action: Bump from 1.x.x → 2.0.0
```

### When to Use MINOR (Feature Addition)
```
Scenario: Add task priority system
- Existing tasks work without priority field
- New API endpoints added, old ones still functional
- Optional database migration for new feature

Action: Bump from 1.0.0 → 1.1.0
```

```
Scenario: Add email notifications
- New background job system
- Existing endpoints unchanged
- New feature doesn't affect task CRUD operations

Action: Bump from 1.0.0 → 1.1.0
```

### When to Use PATCH (Bug Fix/Optimization)
```
Scenario: Fix XSS vulnerability in task rendering
- No API changes
- No data model changes
- Security patch that doesn't alter functionality

Action: Bump from 1.0.0 → 1.0.1
```

```
Scenario: Optimize database query with indexing
- Performance improvement
- Query results identical
- No breaking changes

Action: Bump from 1.0.0 → 1.0.1
```

---

## Docker Image Tagging Strategy

### Tag Naming Convention
```
# Full version (for specific pinning)
nv23046/cc312-flask-to-do-app:1.2.3

# Minor version (allow patch auto-updates)
nv23046/cc312-flask-to-do-app:1.2

# Major version (allow minor/patch auto-updates)
nv23046/cc312-flask-to-do-app:1

# Latest (cutting edge, can be unstable)
nv23046/cc312-flask-to-do-app:latest

# Development (from dev branch)
nv23046/cc312-flask-to-do-app:dev

# Release candidate (testing before prod)
nv23046/cc312-flask-to-do-app:1.2.3-rc1
nv23046/cc312-flask-to-do-app:1.2.3-rc2
```

### Multi-Tag Build Example
```bash
VERSION="1.2.3"
docker build -t nv23046/cc312-flask-to-do-app:$VERSION \
  -t nv23046/cc312-flask-to-do-app:1.2 \
  -t nv23046/cc312-flask-to-do-app:1 \
  -t nv23046/cc312-flask-to-do-app:latest \
  .

# Push all tags
docker push nv23046/cc312-flask-to-do-app --all-tags
```

---

## Integration with CI/CD Pipeline

### GitHub Actions Workflow
```yaml
# .github/workflows/release.yml
name: Release and Build Docker Image

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Extract version from tag
        id: version
        run: |
          VERSION=${GITHUB_REF#refs/tags/v}
          echo "VERSION=${VERSION}" >> $GITHUB_OUTPUT
          echo "Extracted version: $VERSION"
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_HUB_USERNAME }}
          password: ${{ secrets.DOCKER_HUB_PASSWORD }}
      
      - name: Build and push Docker image
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: |
            nv23046/cc312-flask-to-do-app:${{ steps.version.outputs.VERSION }}
            nv23046/cc312-flask-to-do-app:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
      
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ steps.version.outputs.VERSION }}
          body: |
            Docker Image: `nv23046/cc312-flask-to-do-app:${{ steps.version.outputs.VERSION }}`
            Latest Tag: `nv23046/cc312-flask-to-do-app:latest`
```

### GitLab CI Alternative
```yaml
# .gitlab-ci.yml
stages:
  - build
  - release

variables:
  DOCKER_IMAGE_NAME: "nv23046/cc312-flask-to-do-app"

build_docker:
  stage: build
  image: docker:latest
  services:
    - docker:dind
  script:
    - export VERSION=$(echo $CI_COMMIT_TAG | sed 's/v//')
    - docker build -t $DOCKER_IMAGE_NAME:$VERSION -t $DOCKER_IMAGE_NAME:latest .
    - docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD
    - docker push $DOCKER_IMAGE_NAME:$VERSION
    - docker push $DOCKER_IMAGE_NAME:latest
  only:
    - tags
```

---

## Troubleshooting Version Mismatches

### Problem: Docker image version doesn't match Git tag
```bash
# Verify Git tag
git tag -l | grep v1.2.3

# Verify Docker image
docker images | grep cc312-flask-to-do-app

# Solution: Always build immediately after tagging
git tag -a v1.2.3 -m "Release 1.2.3"
git push origin main --tags
VERSION=$(git describe --tags --abbrev=0)
docker build -t nv23046/cc312-flask-to-do-app:${VERSION#v} .
docker push nv23046/cc312-flask-to-do-app:${VERSION#v}
```

### Problem: Overwriting existing tag
```bash
# DO NOT force push tags in production
git tag -a v1.2.3  # ✓ Create new tag
git push origin --tags  # ✓ Push

# AVOID:
git tag -f v1.2.3  # ✗ Force recreate tag
git push origin --force --tags  # ✗ Force push

# If you must fix a tag:
git tag -d v1.2.3 && git push origin :refs/tags/v1.2.3
git tag -a v1.2.3 -m "Release 1.2.3 (corrected)"
git push origin main --tags
```

---

## Version Bump Checklist

Before releasing version X.Y.Z:

- [ ] All PRs merged to dev are tested
- [ ] dev branch merged to main
- [ ] Git tag created: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`
- [ ] Tag pushed: `git push origin main --tags`
- [ ] Docker image built with correct version
- [ ] Docker image tested locally: `docker run nv23046/cc312-flask-to-do-app:X.Y.Z`
- [ ] Image pushed to registry: `docker push --all-tags`
- [ ] GitHub Release page updated with changelog
- [ ] CHANGELOG.md updated
- [ ] dev branch synced with main: `git merge main`
