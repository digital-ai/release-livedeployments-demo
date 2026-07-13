from playwright.sync_api import expect

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
        expect(
            self.page.locator(".external-deployments-card-cell")
            .filter(has_text=deployment_name)
            .first
        ).to_be_visible()
        return self

    def expect_live_deployment_count(
        self, deployment_name: str, count: int
    ) -> "LiveDeploymentsPage":
        deployments = self.page.locator(".external-deployments-card-cell").filter(
            has_text=deployment_name
        )
        expect(deployments).to_have_count(count)
        return self
