# Day 1 of Advent of Code 2021 - part 1

fhand = open('Dec1\input.txt')
prev = int(fhand.readline())
counter = 0
for line in fhand:
    if int(line) > prev:
        counter += 1
    prev = int(line)
print(f"Result: {counter}")
