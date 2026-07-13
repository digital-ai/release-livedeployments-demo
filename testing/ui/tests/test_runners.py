from playwright.sync_api import Page

from pages.remote_runners_page import RemoteRunnersPage


def test_runner_registered_after_setup(authenticated_page: Page) -> None:
    runners_page = RemoteRunnersPage(authenticated_page)
    runners_page.open()
    runners_page.expect_table_page_to_be_visible()
    runners_page.expect_runner_rows_present(minimum_count=1)
