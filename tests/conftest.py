import pytest
from selenium import webdriver

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--environment", action="store", default="dev"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="D:\\Personal\\Python Selenium\\drivers\\chrome\\chromedriver.exe")

    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="D:\\Personal\\Python Selenium\\drivers\\firefox\\geckodriver.exe")

    environment = request.config.getoption("environment")
    if environment == "dev":
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    elif environment == "uat":
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
