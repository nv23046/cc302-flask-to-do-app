import app as app_module


def test_version_endpoint_uses_runtime_version(monkeypatch):
    monkeypatch.setenv("APP_VERSION", "9.9.9")
    assert app_module.get_version() == "9.9.9"


def test_version_endpoint_defaults_to_baked_version(monkeypatch):
    monkeypatch.delenv("APP_VERSION", raising=False)
    assert app_module.get_version() == "2.0.0"


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
