'''
 


'''
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
import pytest

@pytest.fixture
def driver():
    driver=webdriver.Chrome(service=Service((ChromeDriverManager().install())))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("email,password,expected",
                         [
    ("hmgsamir8@gmail.com","123qweasdzxc","success"),
    ("xuxss","123qweasdzxc","failed"),
    ("hmgsamir8@gmail.com","123qweasdzxC","failed"),
    ("","","failed"),
    ],
    ids=[
        "valid login","invalid email","invalid password","empty"
    ]
)
def test_login(driver,email,password,expected):
    driver.get("http://localhost:5173/login")
    email_input=driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']")
    email_input.clear()
    email_input.send_keys(email)
    password_input=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
    password_input.clear()
    password_input.send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    if expected=='success':
        WebDriverWait(driver,5).until(EC.url_contains("owner-dashboard"))
        assert 'owner-dashboard' in driver.current_url
    else:
        WebDriverWait(driver,5).until(EC.url_contains("login"))
        assert "login" in driver.current_url
   
    