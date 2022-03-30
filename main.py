import json
import tweets


def main():
    print(" --- INICIO del programa --- ")
    # Opening JSON file
    f = open('data.json')
    # Creamos las variables que queremos encontrar:
    top_tweets = []
    top_users = []
    top_days = []
    top_hashtags = []

    # returns JSON object as
    # a dictionary
    k = 0
    for line in f:
        data = json.loads(line)
        # print(data["retweetCount"])
        print(top_tweets)
        top_tweets = tweets.top_10_tweets(data, top_tweets)
        k = k + 1
        if k == 100:
            break

    # Closing file
    f.close()
    print(" --- FIN del programa --- ")


main()