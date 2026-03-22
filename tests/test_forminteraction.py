from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_frominteraction(driver):
    driver.get("http://localhost:5173")
    
    driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
    email=driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']")
    email.send_keys("hmgsamir8@gmail.com")
    password=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
    password.send_keys("123qweasdzxc")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    WebDriverWait(driver,10).until(
    EC.url_contains("dashboard")
     )
    current_url=driver.current_url
    assert "owner-dashboard" in current_url ,"dashboard doesnot open"
    logout=driver.find_element(By.XPATH,"//span[normalize-space()='Logout']")
    assert logout.is_displayed()