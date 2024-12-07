import itertools

with open("input.txt") as f:
    total = 0
    while line := f.readline():
        numbers = line.rstrip().split(" ")
        result = numbers[0][:len(numbers[0])-1]
        numbers = numbers[1:]
        permutations = list(itertools.product(['+', '*', '||'], repeat=(len(numbers)-1)))
        everything = []
        numbers_and_operators = []
        for permutation in permutations:
            for number, op in zip(numbers, permutation):
                numbers_and_operators.append(number)
                numbers_and_operators.append(op)
            numbers_and_operators.append(numbers[-1])
            everything.append(numbers_and_operators)
            numbers_and_operators = []
        results = []
        for sequence in everything:
            while len(sequence) != 1:
                first_num = int(sequence[0])
                op = sequence[1]
                second_num = int(sequence[2])
                sequence = sequence[2:]
                if op == '+':
                    sequence[0] = str(first_num+second_num)
                elif op == '*':
                    sequence[0] = str(first_num*second_num)
                elif op == '||':
                    sequence[0] = str(first_num)+str(second_num)
            results.append(sequence[0])
        if result in results:
            total += int(result)
    print(total)
