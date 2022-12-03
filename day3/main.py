from pathlib import Path

def priority(item_type):
    if item_type.isupper():
        return ord(item_type) - 38
    else:
        return ord(item_type) - 96

def part1(rucksack):
    sum = 0

    for rucksack in rucksacks:
        mid = len(rucksack) // 2
        left, right = set(rucksack[:mid]), set(rucksack[mid:])
        for shared_item in left & right:
            sum += priority(shared_item)

    return sum

def part2(rucksacks):
    sum = 0
    groups = [rucksacks[n:n + 3] for n in range(0, len(rucksacks) - 1, 3)]
    for group in groups:
        [a, b, c] = group
        shared_items = set(a) & set(b) & set(c)
        sum += priority(shared_items.pop())

    return sum

input = Path("input.txt").read_text()
rucksacks = input.split('\n')
print("pt1:", part1(rucksacks))
print("pt2:", part2(rucksacks))