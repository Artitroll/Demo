from typing import Union
from data.credentials import User
import allure

from playwright.sync_api import Page, expect


class CustomerPage:
    def __init__(self, page: Page):
        self.page = page
        self.company_table = page.get_by_label("block-item-CardItem-company-")
        self.add_company_button = page.get_by_label("action-Action-Add new-create-")
        self.edit_popup = page.get_by_role("dialog")

        self.details_tab = page.get_by_role("tab", name="Details").locator("div")
        self.notes_tab = page.get_by_role("tab", name="Notes").locator("div")
        self.interactions_tab = page.get_by_role("tab", name="Interactions").locator("div")
        self.orders_tab = page.get_by_role("tab", name="Orders").locator("div")
        self.contacts_tab = page.get_by_role("tab", name="Contacts").locator("div")

    def navigate(self):
        self.page.goto("/admin/6xd1ti4a85d?tab=eauxu34kuux")

    @allure.title("Editing a company")
    def edit_company(self, company_name, page):
        page.get_by_label(f"action-Action.Link-View-view-company-table-{company_name}").click()

    @allure.title("Picking a company")
    def check_company(self, company_name, page):
        cn_cell = page.get_by_role("button", name=company_name, exact=True)
        expect(cn_cell).to_have_count(1)
        company_row = page.locator('.ant-table-row').filter(has=cn_cell)
        expect(company_row).to_have_count(1)
        company_row.get_by_role("button").first.click()
        expect(company_row.get_by_role("checkbox", name="checkbox")).to_be_checked()

    @allure.title("Creating a company")
    def create_company(self, company_name, industry, status,  page):
        page.get_by_label("block-item-CollectionField-company-form-company.name-Name").get_by_role("textbox").fill(
            company_name)
        page.get_by_label("block-item-CollectionField-company-form-company.industry-Industry").get_by_label("down").click()
        page.get_by_role("option", name=industry).locator("div").click()
        page.get_by_label("block-item-CollectionField-company-form-company.status-Status").get_by_label(
            "icon-close-select").click()
        page.get_by_label("block-item-CollectionField-company-form-company.status-Status").get_by_label(
            "down").click()
        page.get_by_text(status, exact=True).click()
        page.get_by_label("action-Action-Submit-submit-").click()
        expect(page.get_by_role("button", name=company_name, exact=True)).to_be_visible()

    @allure.title("Creating a valid company")
    def create_valid_company(self, company_name, page):
        self.create_company(company_name, "Automotive", "Customer", page)

    @allure.title("Validating tabs in view mode")
    def view_tabs(self, page):
        self.interactions_tab.click()
        expect(page.get_by_label("block-item-CardItem-interaction-table")).to_be_visible()
        self.notes_tab.click()
        expect(page.get_by_label("block-item-CardItem-note-list")).to_be_visible()
        self.contacts_tab.click()
        expect(page.get_by_label("block-item-CardItem-contact-")).to_be_visible()
        self.orders_tab.click()
        expect(page.get_by_label("block-item-CardItem-order-")).to_be_visible()
        self.details_tab.click()
        expect(page.get_by_label("block-item-CardItem-company-details")).to_be_visible()
