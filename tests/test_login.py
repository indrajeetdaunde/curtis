import pytest
from selenium.common.exceptions import NoSuchElementException
from page_objects.login_page import LoginPage
from test_data.login_page_data import LoginPageData
from utility.base_class import BaseClass


class TestLogin(BaseClass):

    def test_login(self, get_data):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        log.info("Enter Username")
        login_page.get_username().clear()
        login_page.get_username().send_keys(get_data["username"])
        usr = login_page.get_username().get_attribute('value')
        log.info("Enter Password")
        login_page.get_password().clear()
        login_page.get_password().send_keys(get_data["password"])
        log.info("Click Login button")
        dashboard_page = login_page.click_login_button()

        if usr == "":
            try:
                login_page.get_invalid_credentials_error_msg()
            except NoSuchElementException:
                print("No Such Element")
        elif len(login_page.get_blank_password_error_msgs()) > 0:
            self.verify_link_presence("#Password-error")
            assert login_page.get_blank_password_error_msg().text == "The Password field is required."
        elif len(login_page.get_invalid_credentials_error_msgs()) > 0:
            self.verify_link_presence("div[class='text-danger validation-summary-errors'] ul li")
            assert self.driver.find_element_by_css_selector("div[class='text-danger validation-summary-errors'] ul li"
                                                            ).text == "Invalid username/password"
        else:
            self.verify_link_presence("h3[text()='Dashboard']")
            dashboard_title = dashboard_page.get_dashboard_title().text
            print(dashboard_title)
            assert "OrangeHRM" == dashboard_title
            assert "OrangeHRM" in self.driver.title
            dashboard_page.click_profile().click()
            log.info("Click Logout")
            dashboard_page.click_sign_out().click()
            self.verify_link_presence("h3[class='m-t-20 text-center']")
            # login_title = login_page.get_login_title().text
            # print(login_title)
            # assert "Unified Account Opening" == login_title

        self.driver.refresh()

    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self, request):
        return request.param

