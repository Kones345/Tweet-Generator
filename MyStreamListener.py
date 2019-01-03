import tweepy
import re
import json
import TweetGenerator
import Credentials


# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    # When there is a new tweet detected in the stream it will perform the following actions (generate a new tweet)
    def on_status(self, status):
        my_handle = "@KONADO345 "
        print("HE WHO MADE THE TWEET WAS: ")

        j = json.loads(json.dumps(status._json))
        tweeter = "@" + j["user"]["screen_name"]
        print(tweeter)
        clean = re.sub(my_handle, "", status.text)
        handle_pattern = "@[A-Za-z0-9_]{1,15}"
        handle = re.search(handle_pattern, clean)
        if handle is not None:
            account = handle.group(0)
            account_str = account.replace("@", "")
            tweet = TweetGenerator.generate_tweet(account_str)
            if tweet is None:
                print("COULD NOT GENERATE TWEET")
            else:

                print("TWEET GENERATED WAS: " + tweet)
                Credentials.api.update_status(tweeter + " " + tweet + " - Sent from my Tweet Generator")
        else:
            print("Couldn't find handle")
