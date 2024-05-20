# code to use web scraping to get the users who liked and reposed a tweet
import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time, random, os
from bs4 import BeautifulSoup as bs



def get_tweet_likes(tweet_link):
    # Append /likes to the tweet link
    likes_link = tweet_link + "/likes"
    
    # Set the path to your Firefox profile
    profile = "add profile path here"
    
    # Initialize a Selenium driver with the Firefox profile
    fp = webdriver.FirefoxProfile(profile)
    driver = webdriver.Firefox(firefox_profile=fp)
    
    # Set a random user-agent header
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/109.0 Mobile/15E148 Safari/605.1.15"
    ]
    user_agent = random.choice(user_agents)
    driver.execute_script(f"Object.defineProperty(navigator, 'userAgent', {{value: '{user_agent}'}});")
    
    # Navigate to the likes page
    driver.get(likes_link)
    
    # Simulate some scrolling
    for _ in range(3):
        driver.execute_script("window.scrollBy(0,100)", "")
        time.sleep(random.uniform(1, 5))
    
    # Get the page source
    html = driver.page_source
    
    # Parse the HTML using Beautiful Soup
    soup = bs(html, "html.parser")
    
    # Find all the user cells
    user_cells = soup.find_all("div", class_="css-175oi2r r-ymttw5 r-1f1sjgu r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l")
    
    # Extract the usernames
    usernames = []
    for cell in user_cells:
        username = cell.find("a")["href"].strip("/")
        usernames.append(username)
    
    # Close the Selenium driver
    driver.quit()
    
    return usernames


def get_tweet_retweets(tweet_link):
    # Append /retweets to the tweet link
    retweets_link = tweet_link + "/retweets"
    
    # Set the path to your Firefox profile
    profile = "add path here"
    
    # Initialize a Selenium driver with the Firefox profile
    fp = webdriver.FirefoxProfile(profile)
    driver = webdriver.Firefox(firefox_profile=fp)
    
    # Set a random user-agent header
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/109.0 Mobile/15E148 Safari/605.1.15"
    ]
    user_agent = random.choice(user_agents)
    driver.execute_script(f"Object.defineProperty(navigator, 'userAgent', {{value: '{user_agent}'}});")
    
    # Navigate to the retweets page
    driver.get(retweets_link)
    
    # Simulate some scrolling
    for _ in range(random.randint(2, 5)):
        driver.execute_script("window.scrollBy(0,100)", "")
        time.sleep(random.uniform(2, 5))
    
    # Get the page source
    html = driver.page_source
    
    # Parse the HTML using Beautiful Soup
    soup = bs(html, "html.parser")
    
    # Find all the user cells
    user_cells = soup.find_all("div", class_="css-175oi2r r-ymttw5 r-1f1sjgu r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l")
    
    # Extract the usernames
    usernames = []
    for cell in user_cells:
        username = cell.find("a")["href"].strip("/")
        usernames.append(username)
    
    # Close the Selenium driver
    driver.quit()
    
    return usernames
