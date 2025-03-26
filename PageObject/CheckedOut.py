from selenium.webdriver.common.by import By


class Chcekoutpage:
    def __init__(self, driver):
        self.driver = driver

    # allmobile = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    card_title = (By.CSS_SELECTOR, ".card-title a")
    # self.driver.find_element(By.XPATH, "//button[text()='Add ']")[1].click()
    add_button = (By.XPATH, "//button[text()='Add ']")
    # self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    check_out = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getcardtitle(self):
        return self.driver.find_elements(*Chcekoutpage.card_title)

    def clickaddbutton(self):
        return self.driver.find_elements(*Chcekoutpage.add_button)

    def checkedoutbutton(self):
        return self.driver.find_element(*Chcekoutpage.check_out)
