# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-02-15

### Added
- Task descriptions with rich metadata (priority, due dates, status)
- Task priority levels (Low, Medium, High)
- Task status tracking (To Do, In Progress, Done)
- Advanced filtering by status, priority, and due date ranges
- Search functionality across task titles and descriptions
- Sorting options (newest, due date, priority, title)
- Task tags/labels system with custom colors
- Tag management page with CRUD operations
- Task assignment to multiple tags
- Visual badge system for metadata display
- Filter panel UI with combined filter support
- Task metadata display in list and edit views
- Database schema migrations for new features

### Changed
- Enhanced task list UI with metadata badges
- Improved edit form with additional fields
- Updated database schema with new columns (description, priority, due_date, status, created_at, updated_at)
- Refactored query building for complex filter support

### Technical
- Implemented three feature branches in Gitflow workflow
- Used semantic versioning (MAJOR.MINOR.PATCH)
- Docker image built and tagged with version 0.1.0
- OCI image labels added for metadata
- Health check endpoint integrated

## [1.0.0] - 2026-02-15

### Added
- Initial Flask To-Do application
- Task CRUD operations (Create, Read, Update, Delete)
- Task completion toggle functionality
- SQLite database for task persistence
- Responsive HTML templates
- Docker containerization
- Docker Compose configuration

[Unreleased]: https://github.com/nv23046/cc312-flask-to-do-app/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/nv23046/cc312-flask-to-do-app/compare/v1.0.0...v0.1.0
[1.0.0]: https://github.com/nv23046/cc312-flask-to-do-app/releases/tag/v1.0.0
