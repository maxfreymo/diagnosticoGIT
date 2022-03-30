
def count_user(tweet, users):
    new_user = tweet["user"]["username"]
    #print("Usuario: {}".format(tweet["user"]["username"]))
    # Si el nombre de usuario ya se encuentra en el diccionario, le sumo un tweet al contador
    if users.get(new_user) != None:
        users[new_user] = users[new_user] + 1
    # Si no está en el diccionario, lo agrego con valor inicial 1.
    else:
        users[new_user] = 1
    return users
