import tweepy
import random
import openai

def generate_image():
    # Array of nouns (animals)
    nouns = []
    animal_list = ["cat", "dog", "elephant", "lion", "tiger", "monkey", "giraffe", "zebra", "horse", "rabbit", "cow", "sheep", "bear", "panda", "kangaroo", "dolphin", "shark", "whale", "octopus", "snake"]
    for _ in range(20):
        noun = random.choice(animal_list)
        nouns.append(noun)

    # Array of verbs ending in "-ing"
    verbs = []
    verb_list = ["running", "jumping", "eating", "sleeping", "playing", "singing", "dancing", "reading", "writing", "swimming", "flying", "climbing", "crawling", "hunting", "fighting", "chasing", "exploring", "building", "digging", "cooking"]
    for _ in range(20):
        verb = random.choice(verb_list)
        verbs.append(verb)

    # Array of locations
    locations = []
    location_list = ["beach", "mountain", "forest", "city", "desert", "lake", "river", "island", "cave", "park", "castle", "farm", "jungle", "valley", "ocean", "waterfall", "village", "space", "countryside", "canyon"]
    for _ in range(50):
        location = random.choice(location_list)
        locations.append(location)

    noun = random.choice(nouns)
    verb = random.choice(verbs)
    location = random.choice(locations)

    randprompt = f'A {noun} {verb} in the {location}, 3D render'

    openai.api_key = 'API-KEY'
    response = openai.Image.create(
        prompt=randprompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    return randprompt, image_url
    

# Set your Twitter API credentials
consumer_key = 'USER_Key'
consumer_secret = 'USER_Secret'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Generate and post the image and prompt to Twitter
randprompt, image_url = generate_image()
tweet_text = f"{randprompt}\n{image_url}"

api.update_status(status=tweet_text)