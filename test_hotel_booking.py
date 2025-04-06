from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()  # Or use Service and Options if needed
driver.maximize_window()
driver.get("https://example-hotel-booking.com")  # Replace with real URL

# Step 1: Search for hotels in New York (April 10–15)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "destination"))).send_keys("New York")
driver.find_element(By.ID, "checkin").send_keys("2025-04-10")
driver.find_element(By.ID, "checkout").send_keys("2025-04-15")
driver.find_element(By.ID, "search-btn").click()

# Step 2: Select the first hotel
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hotel-card")))
hotels = driver.find_elements(By.CLASS_NAME, "hotel-card")
if hotels:
    hotels[0].click()
else:
    print("No hotels found.")
    driver.quit()

# Step 3: Apply coupon code
wait.until(EC.presence_of_element_located((By.ID, "coupon-code"))).send_keys("SUMMER25")
driver.find_element(By.ID, "apply-coupon").click()

# Step 4: Verify discount applied
discount = wait.until(EC.presence_of_element_located((By.ID, "discount-value"))).text
assert "25%" in discount or "$" in discount, "Discount not applied as expected"

# Step 5: Proceed to checkout (without payment)
driver.find_element(By.ID, "checkout").click()
print("Test completed: Reached checkout page successfully.")

# Cleanup
time.sleep(2)
driver.quit()
