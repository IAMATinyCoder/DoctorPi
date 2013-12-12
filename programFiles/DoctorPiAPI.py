import tweepy

consumer_key = "Input your conumer_key here"
consumer_secret = "Input your consumer_secret here"
access_token = "Input your access_token here"
access_token_secret = "Input your access_token_secret here"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for page in tweepy.Cursor(api.home_timeline).pages(1):
        for item in page:
                print item.text
