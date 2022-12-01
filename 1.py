f = open("1_input.txt", "rt")

elf_list = []

snack_list = []
for line in  f.readlines():
    if line == '\n':
        elf_list.append(sum(snack_list))
        snack_list = []
    else:
        snack_list.append(int(line.strip()))

task_1 = max(elf_list)
task_2 = sum(sorted(elf_list)[-3:])

