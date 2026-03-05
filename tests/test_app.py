import app as app_module


def test_app_import():
    assert app_module.app is not None


def test_app_responds():
    """Smoke test: app responds to index route."""
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as client:
        response = client.get("/")
    assert response.status_code in [200, 302]
