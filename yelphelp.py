from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
)
    client = Client(auth)
    term = "food"
    params = {
    'term': term,
    'lang': 'en',
    'limit': 3,
    'sort': 2
}
    response = client.search(location, **params)

    businesses = []

    for business in response.businesses:
        businesses.append({"name": business.name,
                           "rating": business.rating,
                           "phone": business.display_phone,
                           "address": business.location.display_address,
                           "url": business.url,
                           "mobile": business.mobile_url,
                           "image": business.image_url,
                           "rate-img": business.rating_img_url_large,
                           "snippet": business.snippet_text,
                           "snip-img": business.snippet_image_url
                           })

    return businesses
