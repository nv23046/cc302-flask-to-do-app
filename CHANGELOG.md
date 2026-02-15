# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Version endpoint (`/api/version`) for health checks
- Version labels in Docker image metadata
- Git workflow documentation (GIT_WORKFLOW.md)
- Docker versioning guide (DOCKER_VERSIONING.md)
- GitHub Actions CI/CD workflows

### Changed
- Updated Dockerfile with OCI labels and healthcheck
- Enhanced app.py with version tracking

## [1.0.0] - 2026-02-15

### Added
- Initial Flask To-Do application
- Task CRUD operations (Create, Read, Update, Delete)
- Task completion toggle functionality
- SQLite database for task persistence
- Responsive HTML templates
- Docker containerization
- Docker Compose configuration

[Unreleased]: https://github.com/nv23046/cc312-flask-to-do-app/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/nv23046/cc312-flask-to-do-app/releases/tag/v1.0.0
