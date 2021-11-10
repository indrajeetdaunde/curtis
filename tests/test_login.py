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
                login_page.get_blank_username_error_msg()
            except NoSuchElementException:
                print("No Such Element")
        elif len(login_page.get_blank_username_error_msgs()) > 0:
            self.verify_text_presence("//span[text()='Username cannot be empty']")
            assert login_page.get_blank_username_error_msg().text == "Username cannot be empty"
        elif len(login_page.get_blank_password_error_msgs()) > 0:
            self.verify_text_presence("//span[text()='Password cannot be empty']")
            assert login_page.get_blank_password_error_msg().text == "Password cannot be empty"
        else:
            self.verify_text_presence("//h1[text()='Dashboard']")
            dashboard_title = dashboard_page.get_dashboard_title().text
            print(dashboard_title)
            # assert "OrangeHRM" == dashboard_title
            assert "OrangeHRM" in self.driver.title
            dashboard_page.click_profile().click()
            log.info("Click Logout")
            self.driver.implicitly_wait(2)
            dashboard_page.click_sign_out().click()
            self.verify_link_presence("#logInPanelHeading")
            login_title = login_page.get_login_title().text
            print(login_title)
            # assert "OrangeHRM" == login_title

        self.driver.refresh()

    @pytest.fixture(params=LoginPageData.test_login_page_data)
    def get_data(self, request):
        return request.param

