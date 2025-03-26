import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class Baseclass:
    def verifylinkpresense(self,text):
        wait = WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located((By.LINK_TEXT,text)))