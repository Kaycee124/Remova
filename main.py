from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chromedriver_path = "path to chromedriver.exe"
# Assign the correct Chrome profile directory
chrome_profile_dir = "path to Chrome profile directory"

# Set up Chrome options with the specified profile directory
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={chrome_profile_dir}")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code
time.sleep(10)

# Print a success message
print("Successfully logged in")

# Keep the window open
