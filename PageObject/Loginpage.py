from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self, driver):
        self.driver = driver #here send the driver variable from the test_e2ewithupdatedata.py
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signin = (By.ID, "signInBtn")

    def login(self,usernames,passwords):
        self.driver.find_element(*self.username).send_keys(usernames)
        self.driver.find_element(*self.password).send_keys(passwords)
        self.driver.find_element(*self.signin).click()
