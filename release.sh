#!/bin/bash

##############################################################################
# Release Script for Flask To-Do Application
# Automates: versioning, git tagging, docker build, and docker push
#
# Usage: ./release.sh 1.1.0
##############################################################################

set -e  # Exit on any error

DOCKER_REGISTRY="nv23046"
DOCKER_IMAGE="cc312-flask-to-do-app"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Helper functions
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

log_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Main script
main() {
    VERSION=$1
    
    if [ -z "$VERSION" ]; then
        log_error "Version argument required"
        echo "Usage: ./release.sh <version>"
        echo "Example: ./release.sh 1.1.0"
        exit 1
    fi
    
    # Validate version format (X.Y.Z)
    if ! [[ $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        log_error "Invalid version format: $VERSION"
        echo "Expected format: X.Y.Z (e.g., 1.1.0)"
        exit 1
    fi
    
    log_info "Starting release process for v${VERSION}..."
    
    # Check git status
    log_info "Checking git status..."
    if ! git diff-index --quiet HEAD --; then
        log_error "Uncommitted changes detected. Commit or stash changes first."
        exit 1
    fi
    
    # Ensure on main branch
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    if [ "$CURRENT_BRANCH" != "main" ]; then
        log_warning "Not on main branch (current: $CURRENT_BRANCH)"
        read -p "Continue anyway? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_info "Release cancelled"
            exit 1
        fi
    fi
    
    # Update version in app.py
    log_info "Updating version in app.py..."
    sed -i "s/__version__ = \"[^\"]*\"/__version__ = \"${VERSION}\"/" app.py
    git add app.py
    git commit -m "chore: bump version to ${VERSION}"
    log_success "Version updated in app.py"
    
    # Create git tag
    log_info "Creating git tag v${VERSION}..."
    git tag -a "v${VERSION}" -m "Release version ${VERSION}"
    log_success "Git tag created"
    
    # Push changes and tags
    log_info "Pushing changes to GitHub..."
    git push origin main
    git push origin --tags
    log_success "Changes and tags pushed"
    
    # Build Docker image
    log_info "Building Docker image..."
    BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
    VCS_REF=$(git rev-parse HEAD)
    
    docker build \
        --build-arg VERSION="${VERSION}" \
        --build-arg BUILD_DATE="${BUILD_DATE}" \
        --build-arg VCS_REF="${VCS_REF}" \
        -t "${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${VERSION}" \
        -t "${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest" \
        .
    log_success "Docker image built"
    
    # Push Docker image
    log_info "Pushing Docker image to Docker Hub..."
    docker push "${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${VERSION}"
    docker push "${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest"
    log_success "Docker image pushed"
    
    # Summary
    echo
    echo -e "${GREEN}============================================${NC}"
    echo -e "${GREEN}✓ Release v${VERSION} Complete!${NC}"
    echo -e "${GREEN}============================================${NC}"
    echo
    echo "Published artifacts:"
    echo "  Git tag:          v${VERSION}"
    echo "  Docker image:     ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${VERSION}"
    echo "  Latest tag:       ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:latest"
    echo
    echo "Next steps:"
    echo "  1. Update CHANGELOG.md with release notes"
    echo "  2. Merge main → dev to sync branches"
    echo "  3. Create GitHub Release from tag: https://github.com/nv23046/cc312-flask-to-do-app/releases"
    echo
}

main "$@"
