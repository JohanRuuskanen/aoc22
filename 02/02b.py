
score_draw_map = {"A": 1, "B": 2, "C": 3}
score_play_map = {"X": 0, "Y": 3, "Z": 6}

def my_move(draw):
    opp, me = draw.split()
    opp = score_draw_map[opp]

    if me == "X":
        score = opp-1 if opp > 1 else 3
    elif me == "Y":
        score = opp
    elif me == "Z":
        score = opp+1 if opp < 3 else 1

    return score

with open("input", "r") as f:
    draws = [line.strip() for line in f.readlines()]

score = []
for draw in draws:
    score.append(score_play_map[draw.split()[1]] + my_move(draw))

print("2b, total score: {}".format(sum(score)))


