from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_venue_distance_filter(driver):
    # 1️⃣ Open the venues page
    driver.get("http://localhost:5173/venues")

    # 2️⃣ Enter a location in the search box (example: Kathmandu)
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Search venues']"))
    )
    search_box.clear()
    search_box.send_keys("Kathmandu")


    # 4️⃣ Wait for venue results to appear
    venue_cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".venue-card"))
    )

    # 5️⃣ For each venue, read its distance and assert ≤ 5 km
    for card in venue_cards:
        distance_text = card.find_element(By.CSS_SELECTOR, ".venue-distance").text  # e.g., "3 km"
        distance_value = float(distance_text.replace("km", "").strip())
        print(f"Venue distance: {distance_value} km")
        assert distance_value <= 5, f"Venue is too far: {distance_value} km"