antennas = {}

with open("input.txt") as f:
    puzzle_input = [list(line) for line in f.read().splitlines()]

for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input[0])):
        current = puzzle_input[i][j]
        if current != ".":
            if current not in antennas:
                antennas[current] = []
            antennas[current].append([i,j])
            
unique_antinodes = set()
for _, positions in antennas.items():
    for position in positions:
        unique_antinodes.add(tuple(position))
        distances_to_positions = [[position[0]-following_position[0], position[1]-following_position[1]] for following_position in positions if following_position != position]
        for distance_to_positions in distances_to_positions:
            antinode_position = [position[0]+distance_to_positions[0], position[1]+distance_to_positions[1]]
            while antinode_position[0] >= 0 and antinode_position[0] < len(puzzle_input) and antinode_position[1] >= 0 and antinode_position[1] < len(puzzle_input[0]):
                unique_antinodes.add(tuple(antinode_position))
                antinode_position = [antinode_position[0]+distance_to_positions[0], antinode_position[1]+distance_to_positions[1]]

print(len(unique_antinodes))
