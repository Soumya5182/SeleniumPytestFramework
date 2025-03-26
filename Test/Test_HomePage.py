import time

from selenium.webdriver.support.select import Select

from PageObject.HomePage import Homepage
from utilities.BaseClass import Baseclass


class TestHomePage(Baseclass):
    def test_formregistration(self):
        # we can be find the element using the name, id ,css selector , classname ,name ,linktest
        homaepage = Homepage(self.driver)
        # driver.find_element(By.NAME, 'email').send_keys("hellosoumya@gmail.com")
        homaepage.Enteremail().send_keys("hellosoumya@gmail.com")
        # driver.find_element(By.ID, 'exampleInputPassword1').send_keys("123456")
        homaepage.Enterpass().send_keys("123456")
        # input the name using the css
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("soumyaranjan")
        homaepage.Entername().send_keys("soumyaranjan")
        # driver.find_element(By.ID, "exampleCheck1").click()
        homaepage.Clickcheckbox().click()
        # here select the drop down the male and female by using the index and testname
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        dropdown = Select(homaepage.Selectdropdown())
        dropdown.select_by_index(1)
        dropdown.select_by_visible_text("Female")
        # submit the button using the xpaTH
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        homaepage.Clicksubmit().click()
        time.sleep(5)
        # find the  sucessfull promt in on click the submit
        # message = driver.find_element(By.CLASS_NAME, "alert-success").text
        message = homaepage.Checkalertmsg().text
        print(message)
        homaepage.Clicksubmit().click()

