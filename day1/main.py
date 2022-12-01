def calcCal(filename):
    with open(filename) as f:
        elves = f.read().split("\n\n")
    return [list(map(int, elf.strip().split("\n"))) for elf in elves]

def partOne(filename):
    elf_calories = calcCal(filename)
    current_max = 0
    for elf in elf_calories:
        if current_max <= sum(elf):
            current_max = sum(elf)
    return current_max

def partTwo(filename):
    elf_calories = calcCal(filename)
    summed_calories = [sum(elf) for elf in elf_calories]
    return sum(sorted(summed_calories, reverse=True)[0:3])

path = "input.txt"
print(partOne(path))
print(partTwo(path))