from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time

@pytest.fixture

def driver():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_loginpage(driver):
      driver.get("http://localhost:5173/")
      
      driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
      time.sleep(2)
      email=driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']")
      email.clear()
      email.send_keys("hmgsamir8@gmail.com")
      password=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
      password.clear()
      password.send_keys("123qweasdzx")
      driver.find_element(By.XPATH,"//button[@type='submit']").click()
      error=WebDriverWait(driver,5).until(
       EC.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Invalid')]"))
      )
      assert error.is_displayed()
      current_url =driver.current_url
      assert "login" in current_url ,"failed the login "
      
      




