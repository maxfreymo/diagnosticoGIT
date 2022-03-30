import json
import tweets
import users
import days
import auxs


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
    top_hashtags = []

    # returns JSON object as
    # a dictionary
    k = 0
    for line in f:
        data = json.loads(line)
        # print(top_tweets)
        #top_tweets = tweets.top_10_tweets(data, top_tweets)
        #users_tweets = users.count_user(data, users_tweets)
        total_days = days.count_days(data, days_tweets)
        k = k + 1
        if k == 1000:
            break

    top_users = auxs.top_ten(users_tweets)
    top_days = auxs.top_ten(total_days)
    print(top_users)
    print(top_days)
    # Closing file
    f.close()
    print(" --- FIN del programa --- ")


main()
