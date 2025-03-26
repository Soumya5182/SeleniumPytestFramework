from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Confirmpage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    ##self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    check_out = (By.XPATH, "//button[@class='btn btn-success']")
    # driver.find_element(By.XPATH, "//input[@id='country']")
    search_country = (By.XPATH, "//input[@id='country']")
    # wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[text()='India']")))
    wait_page = (By.XPATH, "//a[text()='India']")
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    click_check_box = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    click_submit_button = (By.XPATH, "//input[@type='submit']")
    # Sucess_msg = self.driver.find_element(By.CLASS_NAME, "alert-success").text
    sucess_msg = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        return self.driver.find_element(*Confirmpage.check_out)

    def countrysearch(self):
        return self.driver.find_element(*Confirmpage.search_country)

    def waitpage(self):
        return self.wait.until(expected_conditions.presence_of_all_elements_located(Confirmpage.wait_page))

    def clickonindia(self):
        return self.driver.find_element(*Confirmpage.wait_page)

    def checkobx(self):
        return self.driver.find_element(*Confirmpage.click_check_box)

    def submit_button(self):
        return self.driver.find_element(*Confirmpage.click_submit_button)

    def sucessmsgs(self):
        return self.driver.find_element(*Confirmpage.sucess_msg)
