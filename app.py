from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

__version__ = "1.0.0"

app = Flask(__name__)
app.config['VERSION'] = __version__

DATABASE = "todo.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT DEFAULT '',
            priority INTEGER DEFAULT 1,
            due_date DATE,
            status TEXT DEFAULT 'todo',
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    # Create tags table for future feature
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            color TEXT DEFAULT '#0066cc'
        );
    """)
    
    # Create task_tags junction table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS task_tags (
            task_id INTEGER NOT NULL,
            tag_id INTEGER NOT NULL,
            PRIMARY KEY (task_id, tag_id),
            FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
        );
    """)
    
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = get_db()
    search_query = request.args.get("q", "").strip()
    filter_status = request.args.get("status", "").strip()
    filter_priority = request.args.get("priority", "").strip()
    filter_due = request.args.get("due", "").strip()
    sort_by = request.args.get("sort", "created_at").strip()
    
    # Build query
    query = "SELECT * FROM tasks WHERE 1=1"
    params = []
    
    # Search filter
    if search_query:
        query += " AND (title LIKE ? OR description LIKE ?)"
        params.extend([f"%{search_query}%", f"%{search_query}%"])
    
    # Status filter
    if filter_status:
        query += " AND status = ?"
        params.append(filter_status)
    
    # Priority filter
    if filter_priority and filter_priority.isdigit():
        query += " AND priority = ?"
        params.append(int(filter_priority))
    
    # Due date filter
    from datetime import date, timedelta
    today = date.today()
    if filter_due == "overdue":
        query += " AND due_date < ? AND status != 'done'"
        params.append(str(today))
    elif filter_due == "today":
        query += " AND date(due_date) = ?"
        params.append(str(today))
    elif filter_due == "week":
        week_end = today + timedelta(days=7)
        query += " AND due_date BETWEEN ? AND ?"
        params.extend([str(today), str(week_end)])
    
    # Sorting
    sort_options = {
        "created_at": "created_at DESC",
        "due_date": "CASE WHEN due_date IS NULL THEN 1 ELSE 0 END, due_date ASC",
        "priority": "priority DESC",
        "title": "title ASC"
    }
    sort_clause = sort_options.get(sort_by, "created_at DESC")
    query += f" ORDER BY {sort_clause}"
    
    tasks = conn.execute(query, params).fetchall()
    conn.close()
    
    return render_template(
        "index.html", 
        tasks=tasks, 
        version=__version__,
        search_query=search_query,
        filter_status=filter_status,
        filter_priority=filter_priority,
        filter_due=filter_due,
        sort_by=sort_by
    )

@app.route("/api/version")
def version():
    return {"version": __version__, "status": "ok"}

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    description = request.form.get("description", "")
    priority = request.form.get("priority", "1")
    due_date = request.form.get("due_date", None)
    status = request.form.get("status", "todo")

    if title and title.strip():
        conn = get_db()
        conn.execute(
            "INSERT INTO tasks (title, description, priority, due_date, status) VALUES (?, ?, ?, ?, ?)",
            (title.strip(), description, priority, due_date, status)
        )
        conn.commit()
        conn.close()

    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description", "")
        priority = request.form.get("priority", "1")
        due_date = request.form.get("due_date", None)
        status = request.form.get("status", "todo")
        completed = 1 if request.form.get("completed") == "on" else 0

        conn.execute(
            "UPDATE tasks SET title=?, description=?, priority=?, due_date=?, status=?, completed=? WHERE id=?",
            (title, description, priority, due_date, status, completed, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    task = conn.execute(
        "SELECT * FROM tasks WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()
    return render_template("edit.html", task=task)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/toggle/<int:id>", methods=["POST"])
def toggle(id):
    conn = get_db()
    task = conn.execute("SELECT completed FROM tasks WHERE id=?", (id,)).fetchone()
    
    if task:
        new_completed = 0 if task['completed'] else 1
        conn.execute("UPDATE tasks SET completed=? WHERE id=?", (new_completed, id))
        conn.commit()
    
    conn.close()
    return {"success": True, "completed": new_completed if task else None}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)

