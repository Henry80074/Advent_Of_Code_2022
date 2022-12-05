f = open("4_input.txt", "rt")
elf_list = f.readlines()
subset_count = 0
overlap_count = 0
for pair in elf_list:
    elf_assign = pair.strip().split(",")
    section_pair = [elf.split("-") for elf in elf_assign]
    ranges = []
    for section in section_pair:
        section_range = [i for i in range(int(section[0]), int(section[1])+1)]
        ranges.append(section_range)
    if set(ranges[0]).issubset(set(ranges[1])) or set(ranges[1]).issubset(set(ranges[0])):
        subset_count += 1
    if set(ranges[0]).intersection(set(ranges[1])) != set({}):
        overlap_count += 1
print(overlap_count)
