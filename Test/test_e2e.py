import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckedOut import Chcekoutpage
from PageObject.ConfirmPage import Confirmpage
from PageObject.HomePage import Homepage
from utilities.BaseClass import Baseclass





class Testone(Baseclass):
    def test_e2e(self):

        # self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
                             ######|OR|######||
        home_page = Homepage(self.driver)   #here pass our driver varibale because we need our driver varible into our "HomePage.py" pageobject class.Here "Homepage" is the page object class name and "home_page" this object name we declare in our test case.
        home_page.ShopItem().click()
        time.sleep(2)
        # allmobile = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        checkoutpage = Chcekoutpage(self.driver)
        all_mobile = checkoutpage.getcardtitle()
        i= -1
        for mobile in all_mobile:
            i = i + 1
            name = mobile.text
            print(name)
            if name == "Blackberry":
                # self.driver.find_element(By.XPATH, "//button[text()='Add ']")[1].click()
                checkoutpage.clickaddbutton()[i].click()

        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        checkoutpage.checkedoutbutton().click()
        time.sleep(2)
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirmpage = Confirmpage(self.driver)
        confirmpage.checkout().click()
        time.sleep(2)
        # self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
        confirmpage.countrysearch().send_keys("Ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[text()='India']")))
        # confirmpage.waitpage()
        self.verifylinkpresense("India") #its used commonutiles which is define the base call "India" is the parameter passed here.
        # self.driver.find_element(By.XPATH, "//a[text()='India']").click()
        confirmpage.clickonindia().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmpage.checkobx().click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmpage.submit_button().click()
        # Sucess_msg = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        Sucess_msg = confirmpage.sucessmsgs().text
        assert "Thank you! Your order" in Sucess_msg
