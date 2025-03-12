import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open browser
driver = webdriver.Chrome()
time.sleep(3)

# Navigate to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")


# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")

# Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")


# Verify new page URL contains practicetestautomation.com/logged-in-successfully/

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")

# Verify button Log out is displayed on the new page
logout_button_locator = driver.find_element((By.LINK_TEXT, "Log out"))