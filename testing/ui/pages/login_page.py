from playwright.sync_api import Locator, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self, username: str, password: str) -> None:
        self._wait_for_login_form_ready()

        self.page.get_by_placeholder("User").fill(username, timeout=15000)
        self.page.get_by_placeholder("Password").fill(password, timeout=15000)
        self.page.get_by_role("button", name="Log in").click(timeout=10000)
        self.page.wait_for_timeout(1000)
        self._close_pendo_modal_window()

    def _wait_for_login_form_ready(self) -> None:
        user_input = self.page.get_by_placeholder("User")
        password_input = self.page.get_by_placeholder("Password")

        for attempt in range(4):
            self.page.goto("./#/login", wait_until="domcontentloaded")
            expect(self.page).to_have_title("Digital.ai Release")
            self._wait_for_network_idle()

            if self._is_visible(user_input) and self._is_visible(password_input):
                return

            self._reload()
            self.page.wait_for_timeout(500 * (attempt + 1))

        expect(user_input).to_be_visible(timeout=15000)
        expect(password_input).to_be_visible(timeout=15000)

    def _wait_for_network_idle(self) -> None:
        try:
            self.page.wait_for_load_state("networkidle", timeout=5000)
        except Exception:  # noqa: BLE001
            pass

    def _reload(self) -> None:
        try:
            self.page.reload(wait_until="domcontentloaded")
        except Exception:  # noqa: BLE001
            pass

    @staticmethod
    def _is_visible(locator: Locator, timeout: int = 5000) -> bool:
        try:
            return locator.is_visible(timeout=timeout)
        except Exception:  # noqa: BLE001
            return False

    def _close_pendo_modal_window(self) -> None:
        self.page.wait_for_timeout(1000)
        close_button = self.page.locator("._pendo-close-guide")
        if close_button.count() > 0:
            close_button.click()

    def expect_to_be_logged(self, username: str) -> None:
        tooltip = self.page.locator("top-toolbar .avatar-wrapper span.dot-tooltip")
        value = tooltip.get_attribute("aria-label")
        assert value is not None and username in value, (
            f"Expected logged-in user tooltip to contain '{username}', got '{value}'"
        )
