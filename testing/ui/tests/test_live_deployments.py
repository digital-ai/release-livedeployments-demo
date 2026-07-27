import pytest
from playwright.sync_api import Page

from pages.folders_page import FoldersPage
from pages.live_deployments_page import LiveDeploymentsPage


@pytest.mark.phase_one
def test_deploy_deployments_created(authenticated_page: Page) -> None:
    folder_page = FoldersPage(authenticated_page)
    folder_page.open()
    folder_id = folder_page.get_folder_id("Application Demo")
    deployments_page = LiveDeploymentsPage(authenticated_page)
    deployments_page.open(folder_id)
    deployments_page.expect_live_deployment_displayed("Acme-Backend")
    deployments_page.expect_live_deployment_count(
        deployment_name="Acme-Backend", count=4
    )


@pytest.mark.phase_two
def test_argocd_deployment_created(authenticated_page: Page) -> None:
    folder_page = FoldersPage(authenticated_page)
    folder_page.open()
    folder_id = folder_page.get_folder_id("Application Demo")
    deployments_page = LiveDeploymentsPage(authenticated_page)
    deployments_page.open(folder_id)
    deployments_page.expect_live_deployment_displayed("guestbook:guestbook")
    deployments_page.expect_live_deployment_count(
        deployment_name="guestbook:guestbook", count=1
    )


@pytest.mark.phase_two
def test_fluxcd_deployment_created(authenticated_page: Page) -> None:
    folder_page = FoldersPage(authenticated_page)
    folder_page.open()
    folder_id = folder_page.get_folder_id("Application Demo")
    deployments_page = LiveDeploymentsPage(authenticated_page)
    deployments_page.open(folder_id)
    deployments_page.expect_live_deployment_displayed("podinfo:podinfo")
    deployments_page.expect_live_deployment_count(
        deployment_name="podinfo:podinfo", count=1
    )
