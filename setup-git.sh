#!/bin/bash

##############################################################################
# Git Repository Setup Script
# Initializes dev branch, sets up branch protection, and configures workflow
#
# Usage: ./setup-git.sh
##############################################################################

set -e

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

log_error() {
    echo -e "${RED}✗ $1${NC}"
}

main() {
    log_info "Git Repository Setup"
    echo
    
    # Check if on main branch
    CURRENT=$(git rev-parse --abbrev-ref HEAD)
    if [ "$CURRENT" != "main" ]; then
        log_error "Must be on main branch. Current: $CURRENT"
        exit 1
    fi
    
    # Update main
    log_info "Updating main branch..."
    git pull origin main
    log_success "main branch updated"
    
    # Check if dev exists
    if git rev-parse --verify origin/dev > /dev/null 2>&1; then
        log_info "dev branch already exists on remote"
        git checkout dev
        git pull origin dev
    else
        log_info "Creating dev branch from main..."
        git checkout -b dev
        git push -u origin dev
        log_success "dev branch created and pushed"
    fi
    
    # Switch back to main
    git checkout main
    
    # Instructions for branch protection
    echo
    echo -e "${YELLOW}Branch Protection Setup ${NC}"
    echo "────────────────────────────────────"
    echo "Configure branch protection in GitHub:"
    echo
    echo "1. Go to: https://github.com/nv23046/cc312-flask-to-do-app/settings/branches"
    echo
    echo "2. Add protection rule for 'main':"
    echo "   ✓ Require a pull request before merging"
    echo "   ✓ Require status checks to pass"
    echo "   ✓ Require branches to be up to date before merging"
    echo "   ✓ Dismiss stale pull request approvals"
    echo "   ✓ Include administrators in restrictions"
    echo
    echo "3. Add protection rule for 'dev':"
    echo "   ✓ Require a pull request before merging"
    echo "   ✓ Require code reviews"
    echo
    echo -e "${YELLOW}Secrets Setup${NC}"
    echo "────────────────────────────────────"
    echo "Configure secrets in GitHub for Docker Hub authentication:"
    echo
    echo "1. Go to: https://github.com/nv23046/cc312-flask-to-do-app/settings/secrets"
    echo
    echo "2. Add the following secrets:"
    echo "   - DOCKER_HUB_USERNAME: (your Docker Hub username)"
    echo "   - DOCKER_HUB_PASSWORD: (your Docker Hub token or password)"
    echo
    
    # Summary
    echo
    echo -e "${GREEN}Git Setup Complete!${NC}"
    echo "────────────────────────────────────"
    echo "Branches:"
    echo "  main: $(git rev-parse --short main)"
    echo "  dev:  $(git rev-parse --short dev)"
    echo
    echo "Next steps:"
    echo "1. Configure branch protection rules (see above)"
    echo "2. Configure GitHub secrets (see above)"
    echo "3. Start developing: git checkout -b feature/your-feature dev"
    echo
}

main "$@"
