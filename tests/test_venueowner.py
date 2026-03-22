'''
1️⃣ Logs in as a venue owner
2️⃣ Opens Owner Dashboard
3️⃣ Click Add New Venue
4️⃣ Fill in venue details:
Name,Location,Price
Upload image (if applicable)
5️⃣ Submit venue
6️⃣ Assert that the new venue appears in the dashboard list
'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture

def driver():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()



def test_venueowner(driver):
    driver.get("http://localhost:5173/login")
    wait=WebDriverWait(driver,15)
    email=driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']")
    email.clear()
    email.send_keys("hmgsamir8@gmail.com")
    password=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
    password.clear()
    password.send_keys("123qweasdzxc")
    driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Add Venue']"))).click()
    venue_name=driver.find_element(By.XPATH,"//input[@placeholder='Enter venue name']")
    venue_name.send_keys('Palace')
    driver.find_element(By.XPATH,"//input[@placeholder='e.g. Banepa, Kathmandu, etc.']").send_keys("Austrila")
    driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Users\Lenovo\Downloads\palace.jpg")
    driver.find_element(By.XPATH,"//textarea[@placeholder='Describe your venue...']")
    driver.find_element(By.XPATH,"//input[@placeholder='Rs']").send_keys("20000")
    driver.find_element(By.XPATH,"//input[@placeholder='e.g. 100']").send_keys("100")
    from selenium.webdriver import ActionChains

    map_element = wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'gm-style')]")))
# Create action chain to click at offset
    actions = ActionChains(driver)

# Offset from the top-left corner of the map (x, y)
# You can change these values to select different locations
    x_offset = 100
    y_offset = 100

    actions.move_to_element_with_offset(map_element, x_offset, y_offset).click().perform()  
    
    wait.until (EC.element_to_be_clickable(driver.find_element(By.XPATH,"//button[normalize-space()='Save Venue']"))).click()
    time.sleep(1)
    driver.get("http://localhost:5173/owner-dashboard")  # or click the link/button in your app

# Wait until the list loads
    venue_name = "Palace"
    
    venue_element=wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//h3[normalize-space()='{venue_name}']")))
    
    time.sleep(1)
    assert venue_element.is_displayed()
    print(f"✅ Venue '{venue_name}' was successfully added and visible in the list")