import tweepy
import random
import os
import openai

# List of animals, actions, and locations
animals = ["cat", "dog", "elephant", "lion", "tiger", "monkey", "giraffe", "zebra", "horse", "rabbit", "cow", "sheep", "bear", "panda", "kangaroo", "dolphin", "shark", "whale", "octopus", "snake","penguin"]
actions = ["running", "jumping", "eating", "sleeping", "playing", "singing", "dancing", "reading", "writing", "swimming", "flying", "climbing", "crawling", "hunting", "fighting", "chasing", "exploring", "building", "digging", "cooking","skating","biking"]
locations = ["beach", "mountain", "forest", "city", "desert", "lake", "river", "island", "cave", "park", "castle", "farm", "jungle", "valley", "ocean", "waterfall", "village", "space", "countryside", "canyon"]

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"], os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth)

# Set up OpenAI API
openai.api_key = os.environ["DALLE2_API_KEY"]

def get_random_prompt():
    animal = random.choice(animals)
    action = random.choice(actions)
    location = random.choice(locations)
    prompt = f"A {animal} {action} at the {location}"
    return prompt

def generate_dalle2_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        num_images=1
    )
    return response.images[0].url

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