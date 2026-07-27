from playwright.sync_api import expect

from framework.test_util import is_visible_with_reload
from pages.base_page import BasePage


class ReleasesListPage(BasePage):
    def open(self) -> "ReleasesListPage":
        self.page.goto("./#/releases")
        expect(self.page.locator(".release-list")).to_be_visible()
        self.wait_for_releases_loaded()
        return self

    def expect_release_displayed(self, release_title: str) -> "ReleasesListPage":
        expect(
            self.page.locator(".release").filter(has_text=release_title).first
        ).to_be_visible()
        return self

    def expect_release_completed(self, release_title: str) -> "ReleasesListPage":
        release_status = (
            self.page.locator(".release")
            .filter(has_text=release_title)
            .locator(".release-status")
            .filter(has_text="Completed")
        )
        # status does not update automatically without refresh or reload
        is_visible_with_reload(page=self.page, locator=release_status, timeout=180)
        return self

    def clear_all_filters(self) -> "ReleasesListPage":
        clear_all_button = self.page.get_by_test_id("clear-all-btn")
        if clear_all_button.is_visible():
            clear_all_button.click()
        return self

    def wait_for_releases_loaded(self) -> "ReleasesListPage":
        expect(self.page.locator(".releases-list-loaded:visible").first).to_be_visible()
        return self
