def tft_98(h1: list, h2: list, counter=100):
    if len(h1) == 0:
        return "C"
    elif len(h1) >= int(counter - 2):
        return "D"
    counter_d = 0
    for _ in range(len(h2)):
        if h2[_ - 1] == "D":
            counter_d += 1
    if counter_d > round(counter / 13):
        return "D"
    else:
        return h2[len(h2) - 1]