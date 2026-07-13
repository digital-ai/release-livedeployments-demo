from playwright.sync_api import expect

from pages.base_page import BasePage


class ReleasesListPage(BasePage):
    def open(self) -> "ReleasesListPage":
        self.page.goto("./#/releases")
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
        expect(release_status).to_be_visible()
        return self

    def clear_all_filters(self) -> "ReleasesListPage":
        clear_all_button = self.page.get_by_test_id("clear-all-btn")
        clear_all_button.click()

        return self
