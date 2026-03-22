import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

@pytest.fixture

def driver():
     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     yield driver
     driver.quit()
    


def test_openloginpage(driver):
     driver.get("http://localhost:5173")
     driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
     current_url=driver.current_url
     print(current_url)
     assert "login" in current_url,"login page didnot open"