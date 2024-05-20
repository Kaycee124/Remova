import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import time
from bs4 import BeautifulSoup as bs
from utils import write_messages_to_file, read_messages_from_file
import os, sys, time

# Set up your Twitter API credentials
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# ^^^^define important funtions^^^^^


# 1- set profile
profile = "path to your firefox profile here"
fp = webdriver.FirefoxProfile(profile)
driver = webdriver.Firefox(firefox_profile=fp)

# 2- get tmp file location
profiletmp = driver.firefox_profile.path

# but... the current profile is a copy of the original profile :/
print ("running profile " + profiletmp)

driver.get("https://web.whatsapp.com/")
time.sleep(10)

chat_to_open = 'add chat to openhere'

# define the chat i want opened
chat_to_open = chat_to_open

# wait for chat list
wait = WebDriverWait(driver, 30)
chat_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.x1y332i5.x1n2onr6.x6ikm8r.x10wlt62[role='grid']")))


# Find the "TPC FARM 3" group
tpc_farm_3_group = chat_list.find_element(By.XPATH, f"//span[contains(text(), '{chat_to_open}')]")

# Click on the "TPC FARM 3" group
tpc_farm_3_group.click()

# wait for chat window to open



# Wait for the chat window to be present
messages_list = []

# Wait for the chat window to be present
chat_window = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".x3psx0u.xwib8y2.xkhd6sd.xrmvbpv")))

# define the number of messages to retrieve
desired_msg_count = 82
current_msg_count = 0

# Scroll to the top of the chat window
while current_msg_count < desired_msg_count:
    # Scroll up the chat window
    chat_window.send_keys(Keys.HOME)
    time.sleep(1)

    # Get the current number of messages
    messages = chat_window.find_elements(By.CSS_SELECTOR, "div.message-in.focusable-list-item")
    current_msg_count = len(messages)

    print(f"Number of messages found: {current_msg_count}")

# now that we have the desired number of messages, hadn over to beautifulsoup

# once chat window is open, hand over to beautifulsoup
html_content = chat_window.get_attribute("outerHTML")

soup = bs(html_content, 'html.parser')



# Find the messages and retrieve the last 100 messages in the chat window
messages = soup.select('div.message-in.focusable-list-item')[-80:]

if messages:
    print("Messages found")

# assign the number of messages found to current_msg_count
current_msg_count = len(messages)

# retrn number of messages found
print("Number of messages found:", len(messages))



# print the messages
for message in messages:
    try:
        name_element = message.select_one('span._ahxy._ao3e')
        name = name_element.text.strip() if name_element else None
    except AttributeError:
        name = None

    try:
        number_element = message.select_one('span._ahx_')
        number = number_element.text.strip() if number_element else None
    except AttributeError:
        number = None

    try:
        message_element = message.select_one('a._ao3e.selectable-text.copyable-text')
        message = message_element['title'] if message_element else None
    except (AttributeError, KeyError):
        message = None

    # Create dictionary and store data
    chat_info = {
        "name": name,
        "number": number,
        "message": message
    }
    messages_list.append(chat_info)

# print(messages_list)
write_messages_to_file(messages_list)
driver.quit()


