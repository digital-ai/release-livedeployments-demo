from playwright.sync_api import expect

from pages.base_page import BasePage


class FoldersPage(BasePage):
    def open(self) -> "FoldersPage":
        self.page.goto("./#/folders")
        expect(self.page.locator(".folder-list")).to_be_visible()
        self.wait_for_folders_loaded()
        return self

    def get_folder_id(self, folder_name: str) -> str:
        folder = self.page.locator(".folder-row").filter(has_text=folder_name).first
        expect(folder).to_be_visible()
        folder_id = folder.locator("a").get_attribute("href").split("/folders/")[1]
        return folder_id

    def wait_for_folders_loaded(self) -> "FoldersPage":
        expect(self.page.locator(".folder-tree")).to_be_visible()
        expect(self.page.locator(".alert notice")).not_to_be_visible()
        return self
