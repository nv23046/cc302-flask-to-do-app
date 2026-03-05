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
    assert response.status_code in [200, 302]


x = "this line is intentionally too long for flake8 and will fail the CI lint step because it exceeds one hundred and twenty characters"
