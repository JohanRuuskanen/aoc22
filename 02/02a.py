
score_draw_map = {"X": 1, "Y": 2, "Z": 3}
score_map = {
        "A Y": 6, "B Z": 6, "C X": 6, 
        "A X": 3, "B Y": 3, "C Z": 3
        }

with open("input", "r") as f:
    draws = [line.strip() for line in f.readlines()]

score = []
for draw in draws:
    score.append(score_map.get(draw, 0) + score_draw_map[draw.split()[1]])

print("2a, total score: {}".format(sum(score)))


