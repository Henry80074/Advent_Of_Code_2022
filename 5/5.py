stacks = [[['T'],['V'], ['J'], ['W'], ['N'], ['R'], ['M'], ['S']], 
         [['V'],['C'], ['P'], ['Q'], ['J'], ['D'], ['W'], ['B']],
         [['P'],['R'], ['D'], ['H'], ['F'], ['J'], ['B']],
         [['D'],['N'], ['M'], ['B'], ['P'], ['R'], ['F']],
         [['B'],['T'], ['P'], ['R'], ['V'], ['H']],
         [['T'],['P'], ['B'], ['C']],
         [['L'],['P'], ['R'], ['J'], ['B']],
         [['W'],['B'], ['Z'], ['T'], ['L'], ['S'], ['C'], ['N']],
         [['G'],['S'], ['L']]] 
 
f = open("5_input.txt", "rt")
instructions = f.readlines()
for i in instructions:
    numbers = [int(c) for c in i.strip().split() if c.isdigit()]
    first_stack = stacks[numbers[1]-1]
    move_stack = stacks[numbers[1]-1][:numbers[0]]
    # for part b
    # move_stack.reverse()
    new_stack = stacks[numbers[2]-1]
    for i in move_stack:
        new_stack.insert(0, i)
        first_stack.remove(i)
    stacks[numbers[2]-1] = new_stack
    stacks[numbers[1]-1] = first_stack
for i in stacks:
    print(i[0])