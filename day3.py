mem = []

states = ["START", "S1", "S2", "S3", "S4", "N00", "N01", "N02", "C", "N10", "N11", "N12", "END", "D0", "D1", "D2", "D3", "ND2", "ND3", "ND4", "ND5", "ND6"]
state = states[0]

n0 = ""
n1 = ""
ret = 0
enabled = True

with open("input.txt") as f:
    mem = f.read()

for c in mem:
    if state == "START":
        n0 = ""
        n1 = ""
        if c == "m":
            state = "S1"
        elif c == "d":
            state = "D0"
    elif state == "S1":
        n0 = ""
        n1 = ""
        if c == "u":
            state = "S2"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "S2":
        if c == "l":
            state = "S3"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "S3":
        if c == "(":
            state = "S4"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "S4":
        if c >= "0" and c <= "9":
            state = "N00"
            n0 += c
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "N00":
        if c >= "0" and c <= "9":
            state = "N01"
            n0 += c
        elif c == ",":
            state = "C"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "N01":
        if c >= "0" and c <= "9":
            state = "N02"
            n0 += c
        elif c == ",":
            state = "C"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "N02":
        if c == ",":
            state = "C"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "C":
        if c >= "0" and c <= "9":
            state = "N10"
            n1 += c
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "N10":
        if c >= "0" and c <= "9":
            state = "N11"
            n1 += c
        elif c == ")":
            state = "END"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "N11":
        if c >= "0" and c <= "9":
            state = "N12"
            n1 += c
        elif c == ")":
            state = "END"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "N12":
        if c == ")":
            state = "END"
        elif c == "m":
            state = "S1"
        else:
            state = "START"
    elif state == "D0":
        if c == "o":
            state = "D1"
        else:
            state = "START"
    elif state == "D1":
        if c == "(":
            state = "D2"
        elif c == "n":
            state = "ND2"
        else:
            state = "START"
    elif state == "D2":
        state = "START"
        if c == ")":
            enabled = True
    elif state == "ND2":
        if c == "'":
            state = "ND3"
        else:
            state = "START"
    elif state == "ND3":
        if c == "t":
            state = "ND4"
        else:
            state = "START"
    elif state == "ND4":
        if c == "(":
            state = "ND5"
        else:
            state = "START"
    elif state == "ND5":
        state = "START"
        if c == ")":
            enabled = False
    
    if state == "END":
        state = "START"
        if enabled:
            ret += (int(n0) * int(n1))


print(ret)
