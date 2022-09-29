import tweepy,json
import random
import urllib.request
import os.path
access_token = ""
access_token_secret=""
consumer_key=""
consumer_secret=""

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)
count_retweet = int(input("Please enter number of pictures to download : "))
username = str(input("Enter your username : "))
filePath = input('Enter your folder to download : ')
public_tweets = api.home_timeline()
user = api.get_user(screen_name=username)
image_list = api.user_timeline(count = count_retweet + 1)
filePath = filePath or "F:\ela\savefrompython"
def download_image(url,filename):
    fullname = str(filename) + ".jpg"
    pic = urllib.request.urlopen(url)
    print ("downloading " + url)
    completeName = os.path.join(filePath, fullname)
    with open(completeName, "wb") as localFile:
        localFile.write(pic.read())
for item in image_list:
    media_item = item._json
    if 'media' in media_item['entities']:
        for image in media_item['entities']['media']:
            download_image(image['media_url_https'],image['id'])
