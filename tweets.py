# A function that returns the number of retweets


def n_retweets(e):
    return int(e["retweetCount"])


def top_10_tweets(tweet, top_ten):
    print(" El largo de la lista es {}".format(len(top_ten)))
    if len(top_ten) < 10:
        top_ten.append(tweet)
        top_ten.sort(key=n_retweets)

    else:
        if int(tweet["retweetCount"]) > int(top_ten[0]["retweetCount"]):
            a = top_ten.pop(0)
            print(
                "Tweet OUT: {} // Tweet IN: {}".format(n_retweets(a), n_retweets(tweet)))
            top_ten.append(tweet)
            top_ten.sort(key=n_retweets)

    return top_ten
