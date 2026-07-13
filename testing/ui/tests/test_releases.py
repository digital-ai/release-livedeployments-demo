import pytest
from playwright.sync_api import Page

from pages.releases_list_page import ReleasesListPage

# Run release tests first as they make sure that everything was created for other tests


@pytest.mark.phase_one
@pytest.mark.order(1)
def test_deploy_releases_created(authenticated_page: Page) -> None:
    releases_page = ReleasesListPage(authenticated_page)
    releases_page.open()
    releases_page.clear_all_filters()
    releases_page.expect_release_displayed("Deploy Acme-Backend 1.0")
    releases_page.expect_release_completed("Deploy Acme-Backend 1.0")

    releases_page.expect_release_displayed("Add Live Deployments")
    releases_page.expect_release_completed("Add Live Deployments")


@pytest.mark.phase_two
@pytest.mark.order(1)
def test_argocd_releases_created(authenticated_page: Page) -> None:
    releases_page = ReleasesListPage(authenticated_page)
    releases_page.open()
    releases_page.clear_all_filters()
    releases_page.expect_release_displayed("Add ArgoCD Live Deployments")
    releases_page.expect_release_completed("Add ArgoCD Live Deployments")


@pytest.mark.phase_two
@pytest.mark.order(1)
def test_fluxcd_releases_created(authenticated_page: Page) -> None:
    releases_page = ReleasesListPage(authenticated_page)
    releases_page.open()
    releases_page.clear_all_filters()
    releases_page.expect_release_displayed("Add FluxCD Live Deployments")
    releases_page.expect_release_completed("Add FluxCD Live Deployments")
