f = open("3_input.txt", "rt")
sum = 0
for rucksack in  f.readlines():
    rucksack_list = [*rucksack.strip()]
    len_compartment = int(len(rucksack_list)/2)
    part_1 = rucksack_list[:len_compartment]
    part_2 = rucksack_list[len_compartment:]
    dupe = list(set(part_1) & set(part_2))[0]
    if dupe.islower():
        priority = (ord(dupe)-96)
        sum += priority
    else:
        priority = (ord(dupe)-38)
        sum += priority
print(sum)