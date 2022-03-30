
# A function that returns the number of retweets
def n_retweets(e):
    return int(e["retweetCount"])

# A function that returns the second element of a list


def n_elements(e):
    return e[1]


def top_ten(elements):
    lista = list(elements.items())
    lista.sort(reverse=True, key=n_elements)
    top_10 = lista[0:10]
    return top_10
