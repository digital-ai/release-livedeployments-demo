import pytest
from playwright.sync_api import Page

from pages.releases_list_page import ReleasesListPage


@pytest.mark.phase_one
def test_deploy_releases_created(authenticated_page: Page) -> None:
    releases_page = ReleasesListPage(authenticated_page)
    releases_page.open()
    releases_page.clear_all_filters()
    releases_page.expect_release_displayed("Deploy Acme-Backend 1.0")
    releases_page.expect_release_completed("Deploy Acme-Backend 1.0")

    releases_page.expect_release_displayed("Add Live Deployments")
    releases_page.expect_release_completed("Add Live Deployments")
