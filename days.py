

def count_days(tweet, days):
    new_day = (tweet["date"].split('T'))[0]
    #print("Fecha: {}".format(new_day))
    # Si la fecha ya se encuentra en el diccionario, le sumo uno al contador
    if days.get(new_day) != None:
        days[new_day] = days[new_day] + 1
    # Si no está en el diccionario, lo agrego con valor inicial 1.
    else:
        days[new_day] = 1

    return days
