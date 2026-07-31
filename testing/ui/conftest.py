import os
from typing import Iterator

import pytest
from playwright.sync_api import Browser, Page, ViewportSize

from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.environ.get("RELEASE_URL", "http://localhost:5516")


@pytest.fixture(scope="session")
def deploy_url() -> str:
    return os.environ.get("DEPLOY_URL", "http://localhost:4516")


@pytest.fixture(scope="session")
def admin_username() -> str:
    return os.environ.get("ADMIN_USER", "admin")


@pytest.fixture(scope="session")
def admin_password() -> str:
    return os.environ.get("ADMIN_PASSWORD", "admin")


@pytest.fixture(scope="session")
def authenticated_page(
    browser: Browser, admin_username: str, admin_password: str
) -> Iterator[Page]:
    """One shared, already-logged-in page reused by every test in the session."""
    release_url = os.environ.get("RELEASE_URL", "http://localhost:5516")
    context = browser.new_context(
        base_url=release_url, viewport=ViewportSize(width=1920, height=1080)
    )
    page = context.new_page()

    LoginPage(page).login(admin_username, admin_password)

    yield page

    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo
) -> Iterator[None]:
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def _capture_authenticated_page_on_failure(
    request: pytest.FixtureRequest, output_path: str
) -> Iterator[None]:
    if "authenticated_page" not in request.fixturenames:
        yield
        return

    page = request.getfixturevalue("authenticated_page")

    yield

    failed = bool(
        getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    )

    screenshot_option = request.config.getoption("--screenshot")
    capture_screenshot = screenshot_option == "on" or (
        failed and screenshot_option == "only-on-failure"
    )
    if capture_screenshot:
        os.makedirs(output_path, exist_ok=True)
        page.screenshot(path=os.path.join(output_path, "test-failed.png"))
