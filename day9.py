with open("input.txt") as f:
    filesystem = f.read().splitlines()[0]

current_id = 0
sys_map_arr = []
qty_by_ids = {}
for i in range(len(filesystem)):
    val = int(filesystem[i])
    if i % 2 == 0:
        qty_by_ids[current_id] = val
        for j in range(val):
            sys_map_arr.append(current_id)
        current_id += 1
    else:
        for j in range(val):
            sys_map_arr.append(".")

start = 0
end = len(sys_map_arr) - 1

while start < len(sys_map_arr) and sys_map_arr[start] != ".":
    start += 1
while end >= 0 and sys_map_arr[end] == ".":
    end -= 1

while start < len(sys_map_arr) and end >= 0 and start < end:
    sys_map_arr[start] = sys_map_arr[end]
    sys_map_arr[end] = "."
    
    while start < len(sys_map_arr) and sys_map_arr[start] != ".":
        start += 1
    while end >= 0 and sys_map_arr[end] == ".":
        end -= 1

checksum = 0
for idx, c in enumerate(sys_map_arr):
    if c != ".":
        checksum += int(c) * idx
print(checksum)
