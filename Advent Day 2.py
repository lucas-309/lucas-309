score = 8
f = open("abc.txt", "r")
for x in f:
    print(x)
    if x == "A Y":
        score += 8
    if x == "A X":
        score += 4
    if x == "A Z":
        score += 3
    if x == "B X":
        score += 1
    if x == "B Y":
        score += 5
    if x == "B Z":
        score += 9
    if x == "C X":
        score += 7
    if x == "C Y":
        score += 2
    if x == "C Z":
        score += 6

print(score)
