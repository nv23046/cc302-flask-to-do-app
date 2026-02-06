from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

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
            completed BOOLEAN NOT NULL DEFAULT 0
        );
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        conn = get_db()
        conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        conn.commit()
        conn.close()
    return redirect(url_for("index"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()
    if request.method == "POST":
        title = request.form.get("title")
        completed = 1 if request.form.get("completed") == "on" else 0
        conn.execute("UPDATE tasks SET title=?, completed=? WHERE id=?", (title, completed, id))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    task = conn.execute("SELECT * FROM tasks WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("edit.html", task=task)

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
