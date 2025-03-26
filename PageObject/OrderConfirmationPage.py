from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderConfirm:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.ordercheckout = (By.XPATH, "//button[@class='btn btn-success']")
        self.passcountry = (By.XPATH, "//input[@id='country']")
        self.country_click = (By.XPATH, "//a[text()='India']")
        self.click_check_box = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.Submit_button = (By.XPATH, "//input[@type='submit']")
        self.alert_message = (By.CLASS_NAME, "alert-success")

    def checkout(self):
        self.driver.find_element(*self.ordercheckout).click()

    def select_country(self,country):
        self.driver.find_element(*self.passcountry).send_keys(country)
        self.wait.until(expected_conditions.presence_of_all_elements_located(self.passcountry))
    def click_term_and_condition(self):
        self.driver.find_element(*self.click_check_box).click()
    def click_submit_button(self):
        self.driver.find_element(*self.Submit_button).click()
    def alert_messages(self):
        Sucess_msg = self.driver.find_element(*self.alert_message).text
        print(Sucess_msg)
        assert "Success! Thank you!" in Sucess_msg



    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    # driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
    # wait = WebDriverWait(driver, 10)
    # wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[text()='India']")))
    # driver.find_element(By.XPATH, "//a[text()='India']").click()
    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # driver.find_element(By.XPATH, "//input[@type='submit']").click()
    # Sucess_msg = driver.find_element(By.CLASS_NAME, "alert-success").text
    # assert "Thank you! Your order" in Sucess_msg
