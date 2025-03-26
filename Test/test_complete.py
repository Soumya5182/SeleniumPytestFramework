import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckedOut import Chcekoutpage
from PageObject.HomePage import Homepage
from utilities.BaseClass import Baseclass





class Testone(Baseclass):
    def test_e2e(self):

        self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        time.sleep(2)
        allmobile = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for mobile in allmobile:
            name = mobile.find_element(By.XPATH, "div/h4/a").text
            if name == "Blackberry":
                mobile.find_element(By.XPATH, "//button[text()='Add ']").click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[text()='India']")))
        self.driver.find_element(By.XPATH, "//a[text()='India']").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        Sucess_msg = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Thank you! Your order" in Sucess_msg
