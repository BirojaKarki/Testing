import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_checkpagetitle(driver):
     driver.get("http://localhost:5173")
     title=driver.title #gets webpage title
     print(title)
     assert "venue " in title  # check  if the title conatinas the owed venue ans return true or false
     print("Test Passed:Title contains ")
     