with open("input.txt") as f:
    input_str = f.read().split("\n")
    rules = input_str[:input_str.index('')]
    updates = input_str[input_str.index(''):]
    updates = updates[1:len(updates)-1]

rules_dic = {}
for rule in rules:
    key = str(rule[:2])
    if key not in rules_dic:
        rules_dic[key] = []
    rules_dic[key].append(str(rule[3:5]))

incorrect_updates = set()
for update in updates:
    update_elements = update.split(",")
    for element in update_elements:
        element_rules = []
        if element in rules_dic:
            element_rules = rules_dic[element]
        element_updates = update_elements[:update_elements.index(str(element))]
        if len(set(element_rules) & set(element_updates)) > 0:
            incorrect_updates.add(update)

correct_updates = [update.split(',') for update in updates if update not in incorrect_updates]

middle_sum = 0

for correct_update in correct_updates:
    middle_sum += int(correct_update[len(correct_update)//2])

print(middle_sum)
middle_sum = 0

incorrect_updates = [incorrect_update.split(',') for incorrect_update in incorrect_updates]

corrected_updates = []
for incorrect_update in incorrect_updates:
    corrected_update = incorrect_update.copy()
    for i in range(len(corrected_update)):
        for j in range(i):
            if str(corrected_update[i]) in rules_dic and corrected_update[j] in rules_dic[str(corrected_update[i])]:
                corrected_update[i], corrected_update[j] = corrected_update[j], corrected_update[i]
    corrected_updates.append(corrected_update)

for corrected_update in corrected_updates:
    middle_sum += int(corrected_update[len(corrected_update)//2])

print(middle_sum)
