with open("input.txt") as f:
    puzzle_input = [list(line) for line in f.read().splitlines()]

current_pos = [(i, j) for i in range(len(puzzle_input)) for j in range(len(puzzle_input[0])) if puzzle_input[i][j] == "^"] 
current_pos = current_pos[0]

directions = [[-1,0],[0,1],[1,0],[0,-1]]
current_direction = directions[0]

visited_path = 1
encountered_blocks = 0
puzzle_input[current_pos[0]][current_pos[1]] = "X"

next_pos = [current_pos[0]+current_direction[0], current_pos[1]+current_direction[1]]
while next_pos[0] >= 0 and next_pos[0] < len(puzzle_input) and next_pos[1] >= 0 and next_pos[1] < len(puzzle_input[0]):
   if puzzle_input[next_pos[0]][next_pos[1]] == "#":
       current_direction = directions[(directions.index(current_direction)+1)%len(directions)]
       next_pos = [current_pos[0]+current_direction[0], current_pos[1]+current_direction[1]]
       encountered_blocks += 1
   elif puzzle_input[next_pos[0]][next_pos[1]] == ".":
       puzzle_input[next_pos[0]][next_pos[1]] = "X"
       current_pos = [next_pos[0], next_pos[1]]
       next_pos = [current_pos[0]+current_direction[0], current_pos[1]+current_direction[1]]
       visited_path += 1
   elif puzzle_input[next_pos[0]][next_pos[1]] == "X":
       current_pos = [next_pos[0], next_pos[1]]
       next_pos = [current_pos[0]+current_direction[0], current_pos[1]+current_direction[1]]

print(visited_path)
