# imports
import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from cheak import get_tweet_likes
from cheak import get_tweet_retweets
from utils import write_messages_to_file, read_messages_from_file



# data array
filename = "name of file"
data = read_messages_from_file("path to where you store the file"+filename)

whatsapp_to_twitter = []


for dtpoint in data:
    twitter_username = None
    # ensure that the message is not None
    if dtpoint['Message'] is not None:
        if 'twitter.com' in dtpoint['Message']:
            # extract the twitter username from the message
            match = re.search(r'twitter.com/(\w+)', dtpoint['Message'])
            if match:
                twitter_username = "@" + match.group(1)
        elif 'x.com' in dtpoint['Message']:
                match = re.search(r'x.com/(\w+)', dtpoint['Message'])
                if match:
                  twitter_username = "@" + match.group(1)
         # Check if 'Name' and 'Number' keys exist before accessing them and adding them to the list
        if 'Name' in dtpoint :
            name = dtpoint['Name']
        else:
            name = 'find manually in chat'
        if 'Number' in dtpoint:
            number = dtpoint['Number']
        else:
            number = 'find manually in chat'
        
        whatsapp_to_twitter.append({
        'name': name,
        'number': number,
        'twitter_username': twitter_username
             })
        
# print (whatsapp_to_twitter)
# sys.exit('copy this array to the compare.py file and run it to get those who didnt like the tweet')


# second process we want to do.
# checking thtough data array and removing entries that have none link in the message key
# we will use list comprehension to do this

data = [dtpoint for dtpoint in data if dtpoint['Message'] is not None]
# remove entries that are not posts
post_links = [dtpoint for dtpoint in data if 'status' in dtpoint['Message']]

# print (len(post_links))
# sys.exit()

# randomly select n number of elements from the data array as specified 
entries_to_select = 15

import random

selected_entries = random.sample(post_links, entries_to_select)

# from selected entries, use selenuim to go to the link in the message key
profile = "path to your firefox profile here"
fp = webdriver.FirefoxProfile(profile)
# driver = webdriver.Firefox(firefox_profile=fp)

# 2- get tmp file location
# profiletmp = driver.firefox_profile.path
#  get tweet link from selected entries and put only the links in an array
tweet_links_raw = [entry['Message'] for entry in selected_entries]

# strip the link of everything after the question mark and return the link
tweet_links = [re.sub(r'\?.*', '', link) for link in tweet_links_raw]

# getting likes
likers_list = {}

for tweetlink in tweet_links:
    try:
        likes = get_tweet_likes(tweetlink)
        print(f"likes for {tweetlink}: {likes}")
        likers_list[tweetlink] = likes
        # Add a random sleep duration between 15 and 30 seconds
        time.sleep(random.uniform(15, 30))
    except Exception as e:
        print(f"Error scraping {tweetlink}: {e}")
        # Add a shorter sleep duration between 5 and 10 seconds on error
        time.sleep(random.uniform(5, 10))

print ('people that liked:', likers_list)
# merge the likers_list and compare to the whatsapp_to_twitter array to get whatsapp username of users who didnt like the tweet
sys.exit()
# getting retweets
retweets_list = {}

for tweetlink in tweet_links:
    try:
        retweets = get_tweet_retweets(tweetlink)
        print(f"Retweets for {tweetlink}: {retweets}")
        retweets_list[tweetlink] = retweets
        # Add a random sleep duration between 15 and 30 seconds
        time.sleep(random.uniform(15, 30))
    except Exception as e:
        print(f"Error scraping {tweetlink}: {e}")
        # Add a shorter sleep duration between 5 and 10 seconds on error
        time.sleep(random.uniform(5, 10))









