# Tweet Generator

This is a simple program I wrote to reply to Tweets to my twitter account (when the script is running) that contain another user's handle with a Tweet like that user.

Using Twitter's streaming API, my bot will constantly listen for tweets that are @ my account, when there is one and it contains a handle, I use Tweepy to read as many tweets from the account as I can. After pre-processing the tweets by removing things such as punctuation, links and excluding certain tweets, I extract the text from each tweet. This is subsequently passed to the Markovify library which uses Markov models to predict appropriate text of length N characters based on some training data. The training data I provide is the cleaned tweets and the response I tweet back to the user who tweeted my account is a tweet similar to the style of the handle included when tweeting at me.

This was my first experience using the Twitter API and so there was a lot I had to learn to use, however, I really enjoyed seeing what kinds of things twitter makes available for developers to use.

