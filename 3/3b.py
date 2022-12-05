f = open("3_input.txt", "rt")
sum = 0
list_ruck = f.readlines()
groups = [list_ruck[i:i+3] for i in range(0, len(list_ruck), 3)]
for group in groups:
    dupe = list(set([*group[0].strip()]) & set([*group[1].strip()]) & set([*group[2].strip()]))[0]
    if dupe.islower():
        priority = (ord(dupe)-96)
        sum += priority
    else:
        priority = (ord(dupe)-38)
        sum += priority
print(sum)