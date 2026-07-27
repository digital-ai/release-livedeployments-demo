from playwright.sync_api import expect

from framework.test_util import is_visible_with_reload
from pages.base_page import BasePage


class LiveDeploymentsPage(BasePage):
    def open(self, folder_id: str) -> "LiveDeploymentsPage":
        self.page.goto(
            f"./#/folders/{folder_id}/application-pipelines/external-deployments"
        )
        expect(self.page.locator(".external-deployments-table")).to_be_visible()
        self.wait_for_live_deployments_loaded()
        return self

    def wait_for_live_deployments_loaded(self) -> "LiveDeploymentsPage":
        expect(
            self.page.locator(".external-deployments-cards-skeletons")
        ).not_to_be_visible(timeout=30_000)
        return self

    def expect_live_deployment_displayed(
        self, deployment_name: str
    ) -> "LiveDeploymentsPage":
        deployment_card = (
            self.page.locator(".external-deployments-card-cell")
            .filter(has_text=deployment_name)
            .first
        )
        # some deployments take a while to show up
        is_visible_with_reload(
            page=self.page, locator=deployment_card, timeout=120, interval=20
        )
        return self

    def expect_live_deployment_count(
        self, deployment_name: str, count: int
    ) -> "LiveDeploymentsPage":
        deployments = self.page.locator(".external-deployments-card-cell").filter(
            has_text=deployment_name
        )
        # some deployments take a while to show up
        is_visible_with_reload(
            page=self.page, locator=deployments, timeout=120, interval=20
        )
        expect(deployments).to_have_count(count)
        return self
