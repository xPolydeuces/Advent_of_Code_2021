# Day 2 of Advent of Code 2021 - part 2

fhand = open('Dec2\input.txt')
hor, depth, aim = 0, 0, 0
for line in fhand:
    instructions = line.split(" ")
    if instructions[0] == "forward":
        hor += int(instructions[1])
        depth += int(instructions[1]) * aim
    if instructions[0] == "up":
        aim -= int(instructions[1])
    if instructions[0] == "down":
        aim += int(instructions[1])
print(f"Result of multiplying horizontal by depth: {hor*depth}")
