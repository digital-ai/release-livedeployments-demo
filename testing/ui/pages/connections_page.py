from playwright.sync_api import expect

from pages.base_page import BasePage


class ConnectionsPage(BasePage):
    def open(self) -> "ConnectionsPage":
        self.page.goto("./#/configuration")
        expect(
            self.page.get_by_label("breadcrumb").get_by_text("Connections")
        ).to_be_visible()
        return self

    def open_instance(self, instance_name: str) -> "ConnectionsPage":
        expect(self.page.locator("#configuration")).to_be_visible(timeout=200_000)
        instance = self.page.locator(".configuration-instance").filter(
            has_text=instance_name
        )
        expect(instance).to_be_visible()
        instance.locator(".edit-instance").click(force=True)
        return self

    def test_connection(self) -> "ConnectionsPage":
        self.page.get_by_role("button", name="Test").click()
        return self

    def expect_result_banner(self, message: str) -> "ConnectionsPage":
        banner = self.page.locator(".configuration-result-banner")
        expect(banner).to_be_visible(timeout=120_000)
        expect(banner).to_contain_text(message)
        return self
