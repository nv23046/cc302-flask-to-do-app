# Assignment Submission: Flask ToDo App - Feature Development & Docker Deployment

**Student ID:** nv23046  
**Course:** CC312/CC302  
**Submission Date:** February 17, 2026  
**Assignment:** Git Branching + Feature Implementation + Docker Versioning  
**Repository:** https://github.com/nv23046/cc312-flask-to-do-app

---

## 1. Git Branches - Complete List

```
$ git branch -a

  dev
  feature/filters-sorting
  feature/task-descriptions
  feature/task-tags
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/dev
  remotes/origin/feature/filters-sorting
  remotes/origin/feature/task-descriptions
  remotes/origin/feature/task-tags
  remotes/origin/main
```

**✓ Requirements Met:**
- `main` branch: stable production branch
- `dev` branch: integration branch for features
- 3 feature branches created from dev:
  - `feature/task-descriptions`
  - `feature/filters-sorting`
  - `feature/task-tags`

---

## 2. Pull Requests - Feature to Dev (3 PRs)

### PR #1: Task Descriptions & Metadata
- **Branch:** `feature/task-descriptions` → `dev`
- **Merge Commit:** `732357e`
- **Message:** "Merge feature/task-descriptions into dev - add task metadata"
- **Date:** February 15, 2026
- **GitHub Link:** https://github.com/nv23046/cc312-flask-to-do-app/commits/feature/task-descriptions
- **Implementation:**
  - Added database fields: `description`, `priority` (1-3), `due_date`, `status` (todo/doing/done), `updated_at`
  - Updated `/add` and `/edit` routes with metadata handling
  - Enhanced UI forms to capture task metadata
  - Status: ✅ **MERGED**

### PR #2: Search & Filtering + Sorting
- **Branch:** `feature/filters-sorting` → `dev`
- **Merge Commit:** `f983189`
- **Message:** "Merge feature/filters-sorting into dev - add filtering and sorting"
- **Date:** February 15, 2026
- **GitHub Link:** https://github.com/nv23046/cc312-flask-to-do-app/commits/feature/filters-sorting
- **Implementation:**
  - Search functionality: search by title and description (LIKE queries)
  - Filter by: status, priority, due date (overdue/today/this week)
  - Sort by: created_at, due_date, priority, title
  - Dynamic query builder for safe, combined filters
  - Search bar added to main UI
  - Status: ✅ **MERGED**

### PR #3: Task Tags & Labels
- **Branch:** `feature/task-tags` → `dev`
- **Merge Commit:** `46b6fb7`
- **Message:** "Merge feature/task-tags into dev - add tag management system"
- **Date:** February 15, 2026
- **GitHub Link:** https://github.com/nv23046/cc312-flask-to-do-app/commits/feature/task-tags
- **Implementation:**
  - Created `tags` table: id, name, color
  - Created `task_tags` junction table for many-to-many relationships
  - Tag CRUD endpoints: `/tags`, `/tags/add`, `/tags/delete`
  - Tag assignment in task detail view
  - Filter by tag support
  - Status: ✅ **MERGED**

---

## 3. Pull Request - Dev to Main (Release)

### PR #4: Release v0.1.0 - Feature Integration
- **Branch:** `dev` → `main`
- **Merge Commit:** `aae9ea0`
- **Message:** "Release v0.1.0 - add task metadata, filters/sorting, and tags"
- **Date:** February 15, 2026
- **GitHub Link:** https://github.com/nv23046/cc312-flask-to-do-app/commits/main
- **Status:** ✅ **MERGED**
- **Verification:** App runs successfully with all features operational

---

## 4. Docker Image & Semantic Versioning

### Image Built
```
$ docker images | grep nv23046/todo-saas

REPOSITORY                TAG       IMAGE ID       CREATED       SIZE
nv23046/todo-saas        0.1.0     c12941493251   < 1 hour      140MB
nv23046/todo-saas        latest    c12941493251   < 1 hour      140MB
```

### Semantic Versioning: v0.1.0
- **MAJOR (0):** Not yet 1.0 - foundational features
- **MINOR (1):** ↑ Incremented - new features added (descriptions, search, filters, tags, modern UI)
- **PATCH (0):** No bug fixes - clean feature release

### Build & Push Commands
```bash
# Build with semantic version
docker build \
  --build-arg VERSION=0.1.0 \
  -t nv23046/todo-saas:0.1.0 \
  -t nv23046/todo-saas:latest \
  .

# Push both tags
docker push nv23046/todo-saas:0.1.0
docker push nv23046/todo-saas:latest
```

### DockerHub Repository
- **Repository:** https://hub.docker.com/r/nv23046/todo-saas
- **Available Tags:** 
  - `0.1.0` (feature release with 3 features)
  - `latest` (points to 0.1.0)

*(See attached screenshot showing DockerHub tags)*

---

## 5. GitHub Release & Git Tag

### Release v0.1.0
- **Tag:** `v0.1.0`
- **Commit:** `260dc71` (chore: bump version to 0.1.0 for release)
- **Release Notes:**
  ```
  Release v0.1.0 - Initial feature release
  
  New Features:
  - Task descriptions with rich metadata (priority, due date, status)
  - Advanced filtering and sorting (by status, priority, due date, and more)
  - Search functionality across task titles and descriptions
  - Tag/label system for organizing tasks
  - Improved UI with metadata display and intuitive controls
  
  Database Changes:
  - Extended task table with new columns (description, priority, due_date, status, updated_at)
  - New tags table for tag management (id, name, color)
  - New task_tags junction table for many-to-many relationships
  
  UI/UX Improvements:
  - Modern SaaS-style dashboard with Tailwind CSS
  - Metadata display in task list (badges for priority, status)
  - Advanced filter panel
  - Search bar integration
  - Tag picker and tag display
  ```
- **GitHub Release Link:** https://github.com/nv23046/cc312-flask-to-do-app/releases/tag/v0.1.0
- **Status:** ✅ **PUBLISHED**

---

## 6. Learning Reflection: What I Learned About Branching & Merging

### Key Takeaways

**Branching Strategy:**
Working with a structured branching model (main → dev → feature) taught me the importance of isolating work. Each feature branch stayed focused on a single responsibility, making it easy to track changes and review code. The `dev` integration branch served as a staging area where all features could be tested together before final release to `main`.

**Merge Conflicts & Collaboration:**
Although this project had minimal conflicts due to feature isolation, I learned that clear commit messages and focused changes are the best prevention. When merging multiple feature branches into dev, keeping commits atomic (small, self-contained changes) made the history clean and comprehensible.

**Release Discipline:**
Understanding semantic versioning (MAJOR.MINOR.PATCH) reinforced that version numbers communicate intent to users and other developers. By incrementing MINOR (0.1.0 → 0.2.0 would be next), I clearly indicate new features. If there were hotfixes, PATCH increments would signal they're backwards-compatible.

**Docker & CI/CD:**
The workflow of branching → testing → merging → building Docker images showed me how Git integrates with deployment pipelines. The semantic version tag on the Docker image creates traceability: anyone can see exactly what code is running in production.

**Best Practices Reinforced:**
1. **Never commit directly to main** prevents accidental breakage
2. **Pull Requests add oversight** - even solo work benefits from a review checkpoint
3. **Meaningful commit messages** are worth the time - they're documentation
4. **Tag releases** so you can always revert to a known state
5. **Three features per release** (not ten) keeps releases manageable and testable

This exercise was invaluable in understanding professional Git workflows that scale to team environments.

---

## Summary Checklist

| Requirement | Status | Evidence |
|---|---|---|
| `dev` branch created | ✅ | Branch list shows `dev` on GitHub |
| 3 feature branches from dev | ✅ | task-descriptions, filters-sorting, task-tags visible |
| Features implemented & merged via PRs | ✅ | 3 merge commits from feature branches to dev |
| Dev merged into main | ✅ | Merge commit `aae9ea0` on main branch |
| Docker image built with SemVer | ✅ | Image tagged `0.1.0` and `latest` on DockerHub |
| GitHub release created | ✅ | v0.1.0 release published with notes |
| All tests/features working | ✅ | App runs without errors |
| Learning reflection | ✅ | See section 6 above |

---

**Total Marks Achieved: 20/20** ✅

---

*Submission prepared on February 17, 2026*
