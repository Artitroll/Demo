import allure
import pytest
from playwright.sync_api import Page, expect

from data.credentials import User
from pages.login import LoginPage
from pages.customer import CustomerPage


class TestCustomer:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page, base_url):
        self.login_page = LoginPage(page)
        self.login_page.navigate()
        self.login_page.login(User.DEFAULT_USER, User.DEFAULT_USER_PASSWORD)
        expect(page).to_have_url(f"{base_url}/admin/qr6akbz4dxy")
        self.customer_page = CustomerPage(page)
        self.customer_page.navigate()
        yield
        print("this is teardown")


    @allure.title("Check if any customers are present")
    def test_any_present(self, page):
        expect(self.customer_page.company_table).to_be_visible()

    # @allure.title("Check if customers can be sorted")
    # def test_sort(self):
    #     pass
    #
    # @allure.title("Check if customers can be filtered")
    # def test_filter(self):
    #     pass
    #
    @allure.title("Check if customer can be added")
    @pytest.mark.parametrize("company_name", ["test123"])
    def test_add(self, page, company_name):
        self.customer_page.add_company_button.click()
        self.customer_page.create_valid_company(company_name, page)
        expect(page.locator("tbody")).to_contain_text(company_name)


    @allure.title("Check if customer can be added")
    @pytest.mark.parametrize("company_name", ["test123"])
    def test_add_negative(self, page, company_name):
        self.customer_page.add_company_button.click()
        self.customer_page.create_company(company_name, page)
        expect(page.locator("tbody")).to_contain_text(company_name)

    @allure.title("Check if customer can be viewed")
    @pytest.mark.parametrize("company_name", ["Gergold Paper", "Miberty Images"])
    def test_edit(self, page, company_name):
        self.customer_page.edit_company(company_name, page)
        expect(self.customer_page.edit_popup).to_be_visible()
        self.customer_page.view_tabs(page)


    #
    @allure.title("Check if customer can be deleted")
    def test_delete(self, page):
        self.customer_page.check_company("Miberty Images", page)
        # page.get_by_label("table-index-1").click()
        # page.get_by_label("action-Action-Delete-destroy-").click()
        # page.get_by_role("button", name="OK").click()