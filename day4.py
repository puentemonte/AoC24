input_str = []

with open("input.txt") as f:
    input_str = f.read()

puzzle = input_str.split("\n")
puzzle = puzzle[0:len(puzzle)-1]

coords = [[-1, -1],[-1, 0],[-1, 1],[0, -1],[0, 1],[1, -1],[1, 0],[1, 1]]

total_xmas = 0

""" part1:
for i in range(0, len(puzzle)):
    for j in range(0, len(puzzle[0])):
        if puzzle[i][j] == "X":
            for coord in coords:
                xmas = "X"
                for k in range(0, 4):
                    current = [i+coord[0]*k,j+coord[1]*k]
                    if current[0] >= 0 and current[0] < len(puzzle) and current[1] >= 0 and current[1] < len(puzzle[0]):
                        current_value = puzzle[current[0]][current[1]]
                        if len(xmas) == 1 and current_value == "M":
                           xmas += "M"
                        elif len(xmas) == 2 and current_value == "A":
                            xmas += "A"
                        elif len(xmas) == 3 and current_value == "S":
                            xmas += "S"
                            total_xmas += 1
"""
for i in range(0, len(puzzle)):
    for j in range(0, len(puzzle[0])):
        if puzzle[i][j] == "A":
            c0 = [i-1,j-1]
            c1 = [i-1,j+1]
            c2 = [i+1,j-1]
            c3 = [i+1,j+1]
            if c0[0] >= 0 and c0[1] >= 0 and c1[0] >= 0 and c1[1] < len(puzzle) and c2[0] < len(puzzle[0]) and c2[1] >= 0 and c3[0] < len(puzzle[0]) and c3[1] < len(puzzle):
                v0 = puzzle[c0[0]][c0[1]] 
                v1 = puzzle[c1[0]][c1[1]]
                v2 = puzzle[c2[0]][c2[1]] 
                v3 = puzzle[c3[0]][c3[1]] 
                if v0 == "M" and v1 == "M" and v2 == "S" and v3 == "S":
                    total_xmas += 1
                elif v0 == "S" and v1 == "S" and v2 == "M" and v3 == "M":
                    total_xmas += 1
                elif v0 == "M" and v1 == "S" and v2 == "M" and v3 == "S":
                    total_xmas += 1
                elif v0 == "S" and v1 == "M" and v2 == "S" and v3 == "M":
                    total_xmas += 1

print(total_xmas)
