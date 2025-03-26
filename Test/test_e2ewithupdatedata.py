import json
import pytest
from PageObject.Loginpage import Loginpage
from PageObject.OrderConfirmationPage import OrderConfirm
from PageObject.ShopPage import ShopPage


test_data_path = '../data/test_e2ewithupdatedata.json'  #this is the json file path
with open(test_data_path) as f: #At here open the the json file
   test_data = json.load(f) # this is the load method  json data and convert to the python object here "test__data"
   test_list = test_data["data"] # here declare one variable for call the json dictionary key name "Data"


@pytest.mark.parametrize("test_list_item",test_list)   # here call the "test list" whole data and for call the each instance pass the one paramter "test_list_item".
def test_e2e(browserInstance,test_list_item): #Here call the "browserInstance" because we pass the data inside the function.

    driver = browserInstance  #this is call the conftest function
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()

    # this class used for the login page
    login_page = Loginpage(driver)
    login_page.login(test_list_item["userEmail"],test_list_item["userPassword"])

    # this class used for the checd the product out page
    shop_page = ShopPage(driver)
    shop_page.add_product_to_cart(test_list_item["productName"])
    shop_page.check_checkout()

    # this class used for the order confirmation
    confirmation_page = OrderConfirm(driver)
    confirmation_page.checkout()
    confirmation_page.select_country("Ind")
    confirmation_page.click_term_and_condition()
    confirmation_page.click_submit_button()
    confirmation_page.alert_messages()



    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    # driver.find_element(By.XPATH, "//input[@id='country']").send_keys("Ind")
    # wait = WebDriverWait(driver, 10)
    # wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//a[text()='India']")))
    # driver.find_element(By.XPATH, "//a[text()='India']").click()
    # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    # driver.find_element(By.XPATH, "//input[@type='submit']").click()
    # Sucess_msg = driver.find_element(By.CLASS_NAME, "alert-success").text
    # assert "Thank you! Your order" in Sucess_msg
