# code to use firefox instead of chrome

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time

# defining important variables
profile_path = "path to your firefox profile here"
geckodriver_path = "path to your geckodriver here"

# set profile
firefox_profile = webdriver.FirefoxProfile(profile_path)

# set options
firefox_options = Options()
firefox_options.add_argument(f"--profile={profile_path}")
firefox_options.profile = firefox_profile  # set the profile in options
f

# initialize the driver
driver = webdriver.Firefox(service=Service(geckodriver_path), options=firefox_options)

# open whatsapp web
driver.get("https://web.whatsapp.com/")
time.sleep(10)

# print success message
print("Successfully logged in") 