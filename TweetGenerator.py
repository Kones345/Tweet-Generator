#!/usr/bin/python3
import tweepy
import re
import numpy as np
import random
import markovify
import Credentials

tweetStarters = {}
tweetsArray = []
# Cleans up the input tweets
pattern1 = re.compile(
    "^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$")
pattern2 = re.compile("@")


# Gets all tweets from an account and returns the list of all the tweets cleaned
def clean_tweets(username):
    print("username in use in clean tweets: " + username)
    # Loops through all the tweets and adds them to the corpus if they have no links or @s
    for status in tweepy.Cursor(Credentials.api.user_timeline, screen_name="@" + str(username), exclude_replies="true",
                                include_rts="false", tweet_mode='extended').items():
        text = str(status._json['full_text'])
        # print(status._json)
        tokens = text.split()

        if re.search(pattern1, text) is None and re.search(pattern2, text) is None:
            if tokens[0] in tweetStarters.keys():
                tweetStarters[tokens[0]] = (tweetStarters[tokens[0]] + 1)
            else:
                tweetStarters[tokens[0]] = 1
            tweetsArray.append(re.sub(r"http\S+", "", text))

    return " ".join(tweetsArray)


# Makes pairs of words in the corpus
def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])


# Naive Initial attempt
def naive_markov_models(tweets, starting_words_dict):
    # INITIAL MARKOV MODEL ATTEMPT
    # Forms a corpus from the final tweets
    corpus = (" ".join(tweets)).split()
    corpus = [cor for cor in corpus if pattern1.match(cor) == None]

    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    # first_word = np.random.choice(corpus)

    # Starts the tweets with words which are typically used as first words
    starter = random.choice(list(starting_words_dict))

    # Start of Markov chain
    chain = [starter]

    # Average Number of words in a tweet
    n_words = round(len(corpus) / len(tweetsArray))

    # Forms chains by selecting random word from elements of the possible following words
    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    ' '.join(chain)

    return chain


def generate_tweet(handle):
    clean_text = clean_tweets(handle)
    text_model = markovify.Text(clean_text)
    return text_model.make_short_sentence(230)
