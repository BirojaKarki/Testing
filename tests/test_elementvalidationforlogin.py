from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_elementvalidation(driver):
    driver.get("http://localhost:5173/login")
    
    email=driver.find_element(By.XPATH,"//label[normalize-space()='Email Address']")
    password=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
    login_btn=driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']")

    assert email.is_displayed()
    assert password.is_displayed()
    assert login_btn.is_displayed()
