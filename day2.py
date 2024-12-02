safe_reports = 0
levels = []

with open("input.txt") as f:
    levels = f.read().splitlines()
print(len(levels))

for level in levels:
    current_level = level.split(" ")

    safe = True
    first_unsafe = True
    increasing = int(current_level[0]) < int(current_level[1])
    for i in range(len(current_level) - 1):
        diff = abs(int(current_level[i]) - int(current_level[i+1]))
        if diff < 1 or diff > 3:
            # safe = False
            if first_unsafe:
                first_unsafe = False
            else:
                safe = False
        elif increasing and (int(current_level[i]) > int(current_level[i+1])):
            # safe = False
            if first_unsafe:
                first_unsafe = False
            else:
                safe = False
        elif (not increasing) and (int(current_level[i]) < int(current_level[i+1])):
            # safe = False
            if first_unsafe:
                first_unsafe = False
            else:
                safe = False
    if safe:
        safe_reports += 1

print(safe_reports)
