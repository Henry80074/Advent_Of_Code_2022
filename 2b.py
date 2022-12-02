f = open("2_input.txt", "rt")

score_dict = {'X': 0, 'Y': 3, 'Z': 6}
win_dict = {'A': 2, 'B': 3, 'C': 1}
draw_dict = {'A': 1 , 'B': 2, 'C': 3}
lose_dict = {'A': 3 , 'B': 1, 'C': 2}
score = 0
for line in  f.readlines():
    pair = line.strip().split(" ")
    score += score_dict[pair[1]]
    if pair[1] == 'X':
        score += lose_dict[pair[0]]
    elif pair[1] == 'Y':
        score += draw_dict[pair[0]]
    elif pair[1] == 'Z':
        score += win_dict[pair[0]]
print(score)