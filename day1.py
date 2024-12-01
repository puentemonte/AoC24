locationIDs = []
with open('input.txt') as file:
    locationIDs = file.read().splitlines()

left = []
right = []

for location in locationIDs:
    a, b = location.split("   ")
    left.append(a)
    right.append(b)

left.sort()
right.sort()

total_distance = 0

for l, r in zip(left, right):
    total_distance += abs(int(l) - int(r))

print(total_distance)

similarity = 0

for l in left:
    similarity += int(l) * right.count(l)

print(similarity)
