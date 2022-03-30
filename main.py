import json
import tweets
import users
import days
import auxs
import hashtag


def main():
    print(" --- INICIO del programa --- ")
    # Opening JSON file
    f = open('data.json')
    # Creamos las variables que queremos encontrar:
    top_tweets = []
    users_tweets = {}
    top_users = []
    days_tweets = {}
    top_days = []
    hashs = {}
    top_hashtags = []

    # returns JSON object as
    # a dictionary
    k = 0
    for line in f:
        data = json.loads(line)
        top_tweets = tweets.top_10_tweets(data, top_tweets)
        users_tweets = users.count_user(data, users_tweets)
        total_days = days.count_days(data, days_tweets)
        hashs = hashtag.count_hash(data, hashs)
        k = k + 1
        if k == 100000:
            break

    top_users = auxs.top_ten(users_tweets)
    top_days = auxs.top_ten(total_days)
    top_hashtags = auxs.top_ten(hashs)
    print(" Los TOP 10 Tweets son: ")
    print(top_tweets)
    print(" Los TOP 10 Usuarios son: ")
    print(top_users)
    print(" Los TOP 10 Días son: ")
    print(top_days)
    print(" Los TOP 10 Hashtags son: ")
    print(top_hashtags)
    # Closing file
    f.close()
    print(" --- FIN del programa --- ")


main()
