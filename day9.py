with open("input.txt") as f:
    filesystem = f.read().splitlines()[0]

current_id = 0
sys_map_arr = []
qty_by_ids = {}
idx_by_ids = {}
for i in range(len(filesystem)):
    val = int(filesystem[i])
    if i % 2 == 0:
        qty_by_ids[str(current_id)] = val 
        for j in range(val):
            sys_map_arr.append(current_id)
        current_id += 1
    else:
        for j in range(val):
            sys_map_arr.append(".")

""" Part 1
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
"""

for idx, v in enumerate(sys_map_arr):
    if v != "." and str(v) not in idx_by_ids:
        idx_by_ids[str(v)] = idx

file_ids = sorted([int(k) for k in qty_by_ids.keys()], reverse=True)

for current_id in file_ids:
    current_id = str(current_id)
    file_size = qty_by_ids[current_id]
    file_start = idx_by_ids[current_id]
    
    for start in range(file_start):
        if start + file_size <= len(sys_map_arr) and all(sys_map_arr[i] == "." for i in range(start, start + file_size)):
            file_blocks = sys_map_arr[file_start:file_start+file_size]
            
            for i in range(file_start, file_start+file_size):
                sys_map_arr[i] = "."
            
            for i in range(file_size):
                sys_map_arr[start + i] = int(current_id)
            
            break
    
checksum = 0
for idx, c in enumerate(sys_map_arr):
    if c != ".":
        checksum += int(c) * idx
print(checksum)
