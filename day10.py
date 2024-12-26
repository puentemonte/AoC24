arr = []
with open("input.txt") as f:
   arr = f.read().splitlines()

rows, cols = len(arr), len(arr[0])

def dfs(row, col, current_path, reached_nines):
    if int(arr[row][col]) == 9:
        reached_nines.append((row, col))
        return

    current_height = int(arr[row][col])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy

        if (new_row >= 0 and new_row < rows and 
            new_col >= 0 and new_col < cols and
            int(arr[new_row][new_col]) == current_height + 1):

            current_path.append((new_row, new_col))
            dfs(new_row, new_col, current_path, reached_nines)
            current_path.pop()

reachable_nines = 0

for i in range(rows):
    for j in range(cols):
        if arr[i][j] == "0":
            nines_from_this_trailhead = []
            dfs(i, j, [(i, j)], nines_from_this_trailhead)
            if nines_from_this_trailhead:
                reachable_nines += len(nines_from_this_trailhead)

print(reachable_nines)