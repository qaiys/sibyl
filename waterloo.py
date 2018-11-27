set = ['A','B','C']
one = 0
ten = 0
hund = 0
thou = 0

leet = []
for i in range(int(input())):
    leet.append(0)

while True:
    string = [set[thou],set[hund],set[ten],set[one]]
    leet[0] += 1
    if leet[0] == 3:
        leet[0] = 0
        leet[1] += 1
    if leet[1] == 3:
        leet[1] = 0
        leet[2] += 1
    if leet[2] == 3:
        leet[2] = 0
        leet[3] += 1
    if leet[3] == 3:
        break
    print(string)
