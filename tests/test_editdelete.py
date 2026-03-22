import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_editvenue(driver):

    driver.get("http://localhost:5173/login")
    wait=WebDriverWait(driver,15)
    email=driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']")
    email.clear()
    email.send_keys("hmgsamir8@gmail.com")
    password=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
    password.clear()
    password.send_keys("123qweasdzxc")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    venue_name="Palace"
    edit_button=wait.until(EC.element_to_be_clickable((By.XPATH, f"//h3[normalize-space()='Palace']/following::button[contains(text(),'Edit')][1]")))
    edit_button.click()
    update=wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Rs']")))
    update.clear()
    update.send_keys("1")
    
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(3)
     
    displayed_amount = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[4]//div[1]//div[3]//div[1]"))
    )

# If the amount is shown with the 'रु' symbol in a separate span
    amount_number = displayed_amount.text.replace("रु", "").strip()  # remove symbol if present

# Assert the number
    assert amount_number == "1"

def test_delete(driver):
    driver.get("http://localhost:5173/login")
    wait=WebDriverWait(driver,15)
    email=driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']")
    email.clear()
    email.send_keys("hmgsamir8@gmail.com")
    password=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
    password.clear()
    password.send_keys("123qweasdzxc")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    delete_button=wait.until(EC.element_to_be_clickable( (By.XPATH, "//h3[normalize-space()='Palace']/following::button[3]")))
    delete_button.click()
    wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Confirm Delete']"))).click()
    venue_name = "Palace"
    time.sleep(2)
    venue_element=driver.find_elements(By.XPATH, "//h3[normalize-space()='Palace']")
    
    
    assert len(venue_element)==0,f"Venue still exists after deletion"
    print(f"✅ Venue '{venue_name}' was successfully delete")

def test_booking(driver):
    driver.get("http://localhost:5173/login")
    wait=WebDriverWait(driver,15)
    email=driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']")
    email.clear()
    email.send_keys("hmgsamir8@gmail.com")
    password=driver.find_element(By.XPATH,"//input[@placeholder='Enter your password']")
    password.clear()
    password.send_keys("123qweasdzxc")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Booking Requests')]"))).click()
    name= wait.until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Buddha Party Palace')]")))
    name.text
    status=driver.find_element(By.XPATH,"//span[text()='approved']")
    status.text
    if name=="Buddha Party Palace" and status=="approved":
            booked_text = driver.find_element(By.XPATH, ".//span[contains(text(),'Booked')]").text
            assert booked_text.lower() == "booked", f"{name} should be booked!"
            print(f"{name} is approved and booked ✅")
    assert name.is_displayed()
    guests=wait.until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Buddha Party Palace')]/following::div[@class='flex items-center text-gray-600'][normalize-space()='500 guests'][1]")))
    assert guests.is_displayed()
    date=wait.until(EC.presence_of_element_located((By.XPATH,"//h3[contains(text(),'Buddha Party Palace')]/following::div[@class='flex items-center text-gray-600'][normalize-space()='11/6/2025'][1]")))
    assert date.is_displayed()