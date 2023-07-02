import tweepy
import requests
import random
import os

# DALL·E2 API endpoint
DALLE2_API_URL = "https://api.openai.com/v1/images/dalle2/generate"

# List of animals, actions, and locations
animals = ["cat", "dog", "elephant", "lion", "penguin"]
actions = ["running", "reading", "jumping", "sleeping", "eating"]
locations = ["beach", "forest", "mountain", "city", "countryside"]

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"], os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth)

def get_random_prompt():
    animal = random.choice(animals)
    action = random.choice(actions)
    location = random.choice(locations)
    prompt = f"A {animal} {action} at the {location}"
    return prompt

def generate_dalle2_image(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['DALLE2_API_KEY']}"
    }
    data = {
        "prompt": prompt,
        "num_images": 1
    }
    response = requests.post(DALLE2_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["images"][0]["url"]

def tweet_random_dalle2_image():
    prompt = get_random_prompt()
    image_url = generate_dalle2_image(prompt)
    
    # Download the image
    image_data = requests.get(image_url).content
    filename = "dalle2_image.jpg"
    with open(filename, "wb") as f:
        f.write(image_data)
    
    # Tweet the image
    api.update_with_media(filename, status=prompt)
    
    # Remove the downloaded image
    os.remove(filename)

# Tweet a random DALL·E2 image
tweet_random_dalle2_image()