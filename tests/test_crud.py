import sqlite3

import pytest

import app as app_module


@pytest.fixture
def client(tmp_path):
    test_db = tmp_path / "test_todo.db"
    app_module.DATABASE = str(test_db)
    app_module.app.config["TESTING"] = True

    app_module.init_db()

    with app_module.app.test_client() as client:
        yield client


def get_task_id_by_title(title: str) -> int:
    conn = sqlite3.connect(app_module.DATABASE)
    row = conn.execute("SELECT id FROM tasks WHERE title = ? ORDER BY id DESC LIMIT 1", (title,)).fetchone()
    conn.close()
    assert row is not None
    return int(row[0])


def test_create_task(client):
    # Arrange
    payload = {
        "title": "Buy milk",
        "description": "2 liters",
        "priority": "2",
        "status": "todo",
    }

    # Act
    resp = client.post("/add", data=payload, follow_redirects=True)

    # Assert
    assert resp.status_code == 200
    page = resp.get_data(as_text=True)
    assert "Buy milk" in page
    assert "2 liters" in page


def test_update_task(client):
    # Arrange
    client.post(
        "/add",
        data={
            "title": "Old title",
            "description": "old desc",
            "priority": "1",
            "status": "todo",
        },
        follow_redirects=True,
    )
    task_id = get_task_id_by_title("Old title")

    # Act
    resp = client.post(
        f"/edit/{task_id}",
        data={
            "title": "New title",
            "description": "updated desc",
            "priority": "3",
            "status": "doing",
        },
        follow_redirects=True,
    )

    # Assert
    assert resp.status_code == 200
    page = resp.get_data(as_text=True)
    assert "New title" in page
    assert "updated desc" in page
    assert "Old title" not in page


def test_delete_task(client):
    # Arrange
    client.post(
        "/add",
        data={
            "title": "To be deleted",
            "description": "remove this",
            "priority": "1",
            "status": "todo",
        },
        follow_redirects=True,
    )
    task_id = get_task_id_by_title("To be deleted")

    # Act
    resp = client.get(f"/delete/{task_id}", follow_redirects=True)

    # Assert
    assert resp.status_code == 200
    page = resp.get_data(as_text=True)
    assert "To be deleted" not in page
