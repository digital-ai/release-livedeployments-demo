import time

from playwright.sync_api import Page, Locator


def is_visible_with_reload(
    page: Page, locator: Locator, timeout: int = 30, interval: int = 5
) -> bool:
    """
    Reloads the page periodically until the target locator becomes visible.
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        if locator.first.is_visible():
            return True

        page.reload(wait_until="domcontentloaded")
        time.sleep(interval)

    assert (
        False
    ), f"Timeout: Locator '{locator}' did not become visible after {timeout}s"
