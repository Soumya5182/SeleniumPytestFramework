from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self,driver): #here we pass the orginal driver variable from our "test_e2e.py" this is pssed by our constructer.
        self.driver = driver
    shop = (By.XPATH, "//a[text()='Shop']")

    #from here used for test_Homepage.py files for the from registration

    #driver.find_element(By.NAME, 'email').send_keys("hellosoumya@gmail.com")
    email = (By.NAME, 'email')
    #driver.find_element(By.ID, 'exampleInputPassword1').send_keys("123456")
    passd = (By.ID, 'exampleInputPassword1')
    # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("soumyaranjan")
    name = (By.CSS_SELECTOR, "input[name='name']")
    #driver.find_element(By.ID, "exampleCheck1").click()
    checkbox = (By.ID, "exampleCheck1")
    #dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
    dropdown = (By.ID, "exampleFormControlSelect1")
    #driver.find_element(By.XPATH, "//input[@type='submit']").click()
    submit = (By.XPATH, "//input[@type='submit']")
    #message = driver.find_element(By.CLASS_NAME, "alert-success").text
    alrtmsg = (By.CLASS_NAME, "alert-success")
    def ShopItem(self):
        return self.driver.find_element(*Homepage.shop) #Here shop is a class variable we call that in our method name, if you want to see this functionality we can see that in basic leatures.
    # from this method we used for the "Test_HomePage.py" file test case
    def Enteremail(self):
        return self.driver.find_element(*Homepage.email)
    def Enterpass(self):
        return self.driver.find_element(*Homepage.passd)
    def Entername(self):
        return self.driver.find_element(*Homepage.name)
    def Clickcheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)
    def Selectdropdown(self):
        return self.driver.find_element(*Homepage.dropdown)
    def Clicksubmit(self):
        return self.driver.find_element(*Homepage.submit)
    def Checkalertmsg(self):
        return self.driver.find_element(*Homepage.alrtmsg)


