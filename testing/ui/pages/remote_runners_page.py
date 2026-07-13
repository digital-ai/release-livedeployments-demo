from playwright.sync_api import expect

from pages.base_page import BasePage


class RemoteRunnersPage(BasePage):
    def open(self) -> "RemoteRunnersPage":
        self.page.goto("./#/runners")
        return self

    def expect_table_page_to_be_visible(self) -> "RemoteRunnersPage":
        expect(self.page.locator(".remote-runners-table-title h1")).to_contain_text(
            "Digital.ai Release runners"
        )
        expect(self.page.locator("table.dot-table")).to_be_visible()
        return self

    def expect_runner_rows_present(self, minimum_count: int = 1) -> "RemoteRunnersPage":
        rows = self.page.locator("table.dot-table tbody tr")
        expect(rows.first).to_be_visible()

        actual_count = rows.count()
        assert actual_count >= minimum_count, (
            f"Expected at least {minimum_count} runner row(s), found {actual_count}"
        )
        return self

    def expect_runner_visible(self, runner_name: str) -> "RemoteRunnersPage":
        expect(self.page.locator("table.dot-table")).to_contain_text(runner_name)
        return self
