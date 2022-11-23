#  main.py is supposed to be a main bot for the comretition, but we'll see
#  all the content is suposed to be in main() fucntion, but we'll see :)

# h1 for each bot - list of own move

def play(counter=100):
    h1 = []
    h2 = []
    for move in range(counter):
        curr_h1_move = defector(h1, h2)
        curr_h2_move = cooperator(h2, h1)
        h1.append(curr_h1_move)
        h2.append(curr_h2_move)
    return h1, h2


def evaluate(h1, h2):
    if len(h1) != len(h2):
        print('dilo pahne pisunami')
    else:
        score_1 = 0
        score_2 = 0
        for _ in range(len(h1)):
            if h1[_] == "C" and h2[_] == "C":
                score_1 += 2
                score_2 += 1
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


def defector(h1:list, h2:list):
    return "D"


def cooperator(h1:list, h2:list):
    return "C"



def start(counter):
    h1, h2 = play(counter)
    h1_res, h2_res = evaluate(h1, h2)
    print("h1_res =", h1_res)
    print("h2_res =", h2_res)
    for _ in range(len(h1)):
        print("Move number", _, ":", h1[_], h2[_])

if __name__ == "__main__":
    start(100)




