from selenium.webdriver.common.by import By

from page_objects.dashboard_page import DashboardPage


class LoginPage:

    username = (By.CSS_SELECTOR, "#txtUsername")
    password = (By.CSS_SELECTOR, "#txtPassword")
    login_button = (By.CSS_SELECTOR, "#btnLogin")
    login_title = (By.CSS_SELECTOR, "#logInPanelHeading")
    blank_password_error_msg = (By.XPATH, "//span[text()='Password cannot be empty']")
    blank_username_error_msg = (By.XPATH, "//span[text()='Username cannot be empty']")
    invalid_credentials_msg = (By.CSS_SELECTOR, "div[class='text-danger validation-summary-errors'] ul li")

    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.login_button).click()
        dashboard_page = DashboardPage(self.driver)
        # document_upload_pge = ApplicantDocumentUploadPage(self.driver)
        return dashboard_page
        # return document_upload_pge

    def get_login_title(self):
        return self.driver.find_element(*LoginPage.login_title)

    def get_blank_password_error_msgs(self):
        return self.driver.find_elements(*LoginPage.blank_password_error_msg)

    def get_blank_password_error_msgs(self):
        return self.driver.find_elements(*LoginPage.blank_password_error_msg)

    def get_blank_username_error_msgs(self):
        return self.driver.find_elements(*LoginPage.blank_username_error_msg)

    def get_blank_password_error_msg(self):
        return self.driver.find_element(*LoginPage.blank_password_error_msg)

    def get_blank_username_error_msg(self):
        return self.driver.find_element(*LoginPage.blank_username_error_msg)

    def get_invalid_credentials_error_msg(self):
        return self.driver.find_element(*LoginPage.invalid_credentials_msg)
