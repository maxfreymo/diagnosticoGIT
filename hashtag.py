import re


def count_hash(tweet, hashtags):
    new_hashs = re.findall(r'\b#\w+', tweet["content"])
    for h in new_hashs:
        print("Hashtags: {}".format(h))
        # Si el hash ya se encuentra en el diccionario, le sumo uno al contador
        if hashtags.get(h) != None:
            hashtags[h] = hashtags[h] + 1
        # Si no está en el diccionario, lo agrego con valor inicial 1.
        else:
            hashtags[h] = 1

    return hashtags
