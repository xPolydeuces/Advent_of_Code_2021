# Day 2 of Advent of Code 2021 - part 1

fhand = open('Dec2\input.txt')
hor, depth = 0, 0
for line in fhand:
    instructions = line.split(" ")
    if instructions[0] == "forward":
        hor += int(instructions[1])
    if instructions[0] == "up":
        depth -= int(instructions[1])
    if instructions[0] == "down":
        depth += int(instructions[1])
print(f"Result of multiplying horizontal by depth: {hor*depth}")
