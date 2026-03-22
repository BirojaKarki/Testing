'''
Write a Selenium + pytest test that:

1️⃣ Open the homepage and login as a user
2️⃣ Search for a venue (any sample venue)
3️⃣ Click Book / Reserve for the first available venue
4️⃣ Fill in the booking details:
Date
Time
Number of guests
5️⃣ Click Confirm / Book button
6️⃣ Verify booking success:
A confirmation message appears OR
The booking appears in user booking history

'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time


@pytest.fixture

def driver():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_bookingflow(driver):
    driver.get("http://localhost:5173")
    time.sleep(2)
    wait = WebDriverWait(driver, 15)
    # ---------------- Login ----------------
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(2)
    email = driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']")
    email.clear()
    email.send_keys("hmgsamir8@gmail.com")
    password = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
    password.clear()
    password.send_keys("123qweasdzxc")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # ---------------- Open Venues ----------------
    driver.find_element(By.XPATH, "//button[normalize-space()='Venues']").click()
    time.sleep(1)

    # ---------------- Book first venue ----------------
    driver.find_element(By.XPATH, "//section[@class='py-12']//div[@class='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8']//div[1]//div[2]//button[1]").click()
    time.sleep(2)

    # ---------------- Fill Booking Details ----------------
    # Select date
    driver.find_element(By.XPATH, "//div[@aria-label='Choose Friday, March 13th, 2026']").click()
    # You can add time and guest selection here if applicable

    # ---------------- Mock Khalti Payment ----------------
    # Check if Khalti button exists (it won't in Selenium due to security)
    button = driver.find_element(By.XPATH, "//button[contains(text(),'Khalti')]")
    #print("Khalti buttons found:", len(button))
    button.click()
    time.sleep(2)
    current_url=driver.current_url
    print(current_url)
    time.sleep(2)
    
    driver.find_element(By.XPATH,"//button[@aria-label='EBANKING']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[div[contains(text(),'Agricultural Development Bank')]]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@inputmode='numeric']").send_keys("9800000001")
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='css-175oi2r r-1awozwy r-18u37iz r-1777fci r-eu3ka r-3pj75a']").click()

    current_url=driver.current_url
    assert "http://localhost:5173/payment/?status=Completed&t=txn" in current_url,"No sucessfull"
    print(current_url)