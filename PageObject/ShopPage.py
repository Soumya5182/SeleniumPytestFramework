from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self,driver):
        self.driver = driver

        self.click_shop = (By.XPATH, "//a[text()='Shop']")
        self.check_mobile_names = (By.XPATH, "//div[@class='card h-100']")
        self.check_one_mobile = (By.XPATH, "div/h4/a")
        self.click_on_add = (By.XPATH, "div/button")
        self.click_on_checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def add_product_to_cart(self,mobilename):

        self.driver.find_element(*self.click_shop).click()
        allmobile = self.driver.find_elements(*self.check_mobile_names)
        for mobile in allmobile:
            name = mobile.find_element(*self.check_one_mobile).text
            if name == mobilename:
                mobile.find_element(*self.click_on_add).click()

    def check_checkout(self):  # this  is the another method to call t
        self.driver.find_element(*self.click_on_checkout).click()

