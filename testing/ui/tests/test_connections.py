import pytest
from playwright.sync_api import Page

from pages.connections_page import ConnectionsPage


@pytest.mark.phase_one
def test_deploy_connection(authenticated_page: Page) -> None:
    connections_page = ConnectionsPage(authenticated_page)
    connections_page.open()
    connections_page.open_instance("Local Deploy (Docker)")
    connections_page.test_connection()
    connections_page.expect_result_banner(
        "Digital.ai Deploy Server (Container) is available"
    )


@pytest.mark.phase_two
def test_kubernetes_connection(authenticated_page: Page) -> None:
    connections_page = ConnectionsPage(authenticated_page)
    connections_page.open()
    connections_page.open_instance("Kubernetes Server Connection")
    connections_page.test_connection()
    connections_page.expect_result_banner("Kubernetes API Server (Container)")


@pytest.mark.phase_two
def test_argocd_connection(authenticated_page: Page) -> None:
    connections_page = ConnectionsPage(authenticated_page)
    connections_page.open()
    connections_page.open_instance("ArgoCD Server Connection")
    connections_page.test_connection()
    connections_page.expect_result_banner("ArgoCD API Server (Container) is available")


@pytest.mark.phase_two
def test_fluxcd_connection(authenticated_page: Page) -> None:
    connections_page = ConnectionsPage(authenticated_page)
    connections_page.open()
    connections_page.open_instance("FluxCD Server Connection")
    connections_page.test_connection()
    connections_page.expect_result_banner("FluxCD API Server (Container) is available")
