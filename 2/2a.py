f = open("2_input.txt", "rt")

score_dict = {'X': 1, 'Y': 2, 'Z': 3}
win_dict = {'A': 'Y', 'B': 'Z', 'C':'X' }
match_dict = {'A': 'X', 'B': 'Y', 'C':'Z' }
score = 0
for line in  f.readlines():
    pair = line.strip().split(" ")
    score += score_dict[pair[1]]
    if match_dict[pair[0]] == pair[1]:
        score += 3
    if win_dict[pair[0]] == pair[1]:
        score += 6
    else:
        pass
print(score)