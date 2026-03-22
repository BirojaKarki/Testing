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
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_venuesearchtest(driver):
    driver.get("http://localhost:5173/venues")
    time.sleep(2)
    search=driver.find_element(By.XPATH,"//input[@placeholder='Search venues or locations...']")
    search_term="Biroja"
    search.send_keys(search_term)
    time.sleep(2)
    
    results = WebDriverWait(driver,5).until(
        EC.presence_of_all_elements_located((By.XPATH,"//*[contains(text(),'(search_term)')]"))
    )
    assert len(results)>0,"No venue found"
