stones = [num for num in open("input.txt").read().split(" ")]

""" Part 1
for _ in range(25):
    stones_copy = []
    for idx in range(len(stones)):
        stone = stones[idx]
        if stone == "0":
            stones_copy.append("1")
        elif len(stone) % 2 == 0:
            stones_copy.append(str(int(stone[:len(stone)//2])))
            stones_copy.append(str(int(stone[len(stone)//2:])))
        else:
            stones_copy.append(str(int(stone)*2024))
    stones = stones_copy.copy()

print(len(stones))
"""


def calc(stone, steps):
    if steps == 0:
        return 1
    elif stone == "0":
        return calc("1", steps - 1)
    elif len(stone) % 2 == 0:
        return calc(str(int(stone[:len(stone)//2])), steps - 1) + calc(str(int(stone[len(stone)//2:])), steps - 1)
    else:
        return calc(str(int(stone)*2024), steps - 1)

print(sum(calc(stone, 75) for stone in stones))