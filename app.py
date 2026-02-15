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
    
    if search_query:
        # Search by title or description
        tasks = conn.execute(
            "SELECT * FROM tasks WHERE title LIKE ? OR description LIKE ? ORDER BY created_at DESC",
            (f"%{search_query}%", f"%{search_query}%")
        ).fetchall()
    else:
        tasks = conn.execute("SELECT * FROM tasks ORDER BY created_at DESC").fetchall()
    
    conn.close()
    return render_template("index.html", tasks=tasks, version=__version__, search_query=search_query)

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

