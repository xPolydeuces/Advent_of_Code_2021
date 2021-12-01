# Day 1 of Advent of Code 2021 - part 2

fhand = open('Dec1\input.txt')
prev = None
current = 0
file_end = False
mov = 0
counter = 0
measurements_list = []
for line in fhand:
    measurements_list.append(int(line))
while file_end is False:
    for i in measurements_list[mov:mov+3]:
        current += i
    mov += 1
    if prev is None:
        prev = current
        continue
    elif current > prev:
        counter += 1
    if current == 0:
        file_end = True
    prev = current
    current = 0
print(f"Result: {counter}")
