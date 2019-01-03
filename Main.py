
import tweepy
from MyStreamListener import MyStreamListener
import Credentials

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=Credentials.api.auth, listener=myStreamListener)

# Loops the stream if there is an error in the stream we just start streaming again
while True:
    try:
        myStream.filter(track=['@KONADO345'])
    except Exception:
        print("Tried to break but still here")
        continue
