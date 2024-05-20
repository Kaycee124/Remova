# rubbish code. ignore {twitter seems to have deprecated api endpoints for free users}
# twitter checker file will export functions that do alot of the checking

# get liking users

import os, json, time, sys, requests, base64

# bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

def get_bearer_token(consumer_key, consumer_secret):
    """
    Obtains an App-only Access Token (Bearer Token) from the Twitter API.

    Args:
        consumer_key (str): Your Twitter API consumer key.
        consumer_secret (str): Your Twitter API consumer secret.

    Returns:
        str: The App-only Access Token (Bearer Token).
    """
    # Step 1: Calculate the Base64-encoded "consumer_key:consumer_secret"
    credentials = f"{consumer_key}:{consumer_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    # Step 2: Obtain the App-only Access Token (Bearer Token)
    token_url = "https://api.twitter.com/oauth2/token"
    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(token_url, headers=headers, data=data)
    response.raise_for_status()
    bearer_token = response.json()["access_token"]

    return bearer_token


bearer_token = get_bearer_token(consumer_key, consumer_secret)
print (bearer_token)

def create_url(id):
    url = "https://api.twitter.com/2/tweets/{}/liking_users".format(id)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2LikingUsersPython"
    return r


def connect_to_endpoint(url, bearer_token ):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def get_likes (id):
  url = create_url(id)
  json_response = connect_to_endpoint(url, bearer_token)
  response = (json.dumps(json_response, indent=4, sort_keys=True))
  return response


get_likes(tweet_id)

def extract_tweet_id(link_array):
    tweet_ids = []
    for link in link_array:
        if 'twitter.com' in link:
            # Twitter link
            tweet_id = re.search(r'/status/(\d+)', link)
            if tweet_id:
                tweet_ids.append(tweet_id.group(1))
        elif 'x.com' in link:
            # X.com link
            tweet_id = re.search(r'/status/(\d+)', link)
            if tweet_id:
                tweet_ids.append(tweet_id.group(1))
    return tweet_ids


tweet_ids = extract_tweet_id()

def get_tweet_likes_by_id (tweet_ids):
    for id in tweet_ids:
        likes = get_likes(id)
        # store the likes in a file making sure that likes array is marked by the id used
        with open('likes.txt', 'a') as file:
            file.write(f'{id}: {likes}\n')
        print ('done')
        # sleep for 5 seconds to avoid rate limiting
        time.sleep(5)

get_tweet_likes_by_id(tweet_ids)