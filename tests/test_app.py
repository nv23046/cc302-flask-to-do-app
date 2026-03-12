import app as app_module


def test_app_import():
    assert app_module.app is not None


def test_app_responds(tmp_path):
    """Smoke test: app responds to index route."""
    test_db = tmp_path / "test_todo.db"
    app_module.DATABASE = str(test_db)
    app_module.init_db()

    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        response = client.get("/")
    assert response.status_code == 201
