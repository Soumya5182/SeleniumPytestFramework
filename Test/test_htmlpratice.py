import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_e2e(browserInstance):

    driver = browserInstance
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
    driver.find_element(By.ID,"password").send_keys("learning")
    driver.find_element(By.ID,"signInBtn").click()
    driver.find_element(By.XPATH, "//a[text()='Shop']").click()
    allmobile = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for mobile in allmobile:
        name = mobile.find_element(By.XPATH, "div/h4/a").text
        if name == "Blackberry":
            mobile.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[text()='India']")))
    driver.find_element(By.XPATH, "//a[text()='India']").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    Sucess_msg = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(Sucess_msg)
    assert "Thank you! Your order" in Sucess_msg



#-----------------------conftest.py-----------------------------
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None #this is the global driver variable we can declare this variable in all the functions

# this method used for the run with the diffrent browser using pass the command line argument.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



#####this conftesttest fixture used for the teste2ewithupdatedata.py test case####
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    global driver
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    yield driver
    driver.close()


###########for take the screenshots in html report we used this function ##########################



@pytest.hookimpl(hookwrapper=True)
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
            reports_dir = os.path.join(os.path.dirname(__file__), 'Htmlreport')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)  #this is the driver function to take the screenshot