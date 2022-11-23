#  main.py is supposed to be a main bot for the comretition, but we'll see
#  all the content is suposed to be in main() fucntion, but we'll see :)

# h1 for each bot - list of own move

def play(counter=100):
    players = {defector: 0, cooperator: 0, tft: 0, tft_99: 0}
    pairs = [(a, b) for idx, a in enumerate(list(players.keys())) for b in list(players.keys())[idx + 1:]]
    with open("results.txt", "w") as f:
        for pair in pairs:
            h1 = []
            h2 = []
            for move in range(counter):
                curr_h1_move = pair[0](h1, h2, counter)
                curr_h2_move = pair[1](h2, h1, counter)
                h1.append(curr_h1_move)
                h2.append(curr_h2_move)
            score1, score2 = evaluate(h1, h2)       
            f.write(str(pair[0].__name__) + " and " + str(pair[1].__name__) + ":" +"\n")
            f.write("score: " + str(score1) + ", " + str(score2) +"\n")
            for i in range(len(h1)):
                f.write("Move number " + str(i) + ": " + str(h1[i]) + ", " + str(h2[i]) +"\n")
            players[pair[0]] += score1
            players[pair[1]] += score2
            f.write("\n")
            f.write("\n")
            # print("result for pair", str(pair[0].__name__), str(pair[1].__name__), "is:", score1, score2)
        
        # create new dictionary to white the results 
        results = {}
        for ele in players.keys():
            results[str(ele.__name__)] = players[ele]
        results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))
        f.write('overall results: ' + str(results))


def evaluate(h1, h2):
    if len(h1) != len(h2):
        print('dilo pahne pisunami')
    else:
        score_1 = 0
        score_2 = 0
        for _ in range(len(h1)):
            if h1[_] == "C" and h2[_] == "C":
                score_1 += 2
                score_2 += 2
            elif h1[_] == "C" and h2[_] == "D":
                score_1 -= 1
                score_2 += 3
            elif h1[_] == "D" and h2[_] == "C":
                score_1 += 3
                score_2 -= 1
            elif h1[_] == "D" and h2[_] == "D":
                pass
            else:
                print(h1[_], h2[_], "??????????????")
    return score_1, score_2


def defector(h1:list, h2:list, counter=100):
    return "D"


def cooperator(h1:list, h2:list, counter=100):
    return "C"


def tft(h1:list, h2:list, counter=100):
    if len(h1) == 0:
        return "C"
    else:
        return h2[len(h2) - 1]

def tft_99(h1:list, h2:list, counter=100):
    if len(h1) == 0:
        return "C"
    elif len(h1) == counter - 1:
        return "D"
    else:
        return h2[len(h2) - 1]

# def log(counter):
#     h1, h2 = play(counter)
#     h1_res, h2_res = evaluate(h1, h2)
#     print("h1_res =", h1_res)
#     print("h2_res =", h2_res)
#     for _ in range(len(h1)):
#         print("Move number", _, ":", h1[_], h2[_])

if __name__ == "__main__":
    play(50)




