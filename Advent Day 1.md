temp = 0 
sum = 0

f = open("ab.txt", "r")
for x in f:
  if x != "\n":
    temp += int(x)
  else:
    temp = 0
  if temp > sum:
    sum = temp

print(sum)

temp = 0 
sum = 0
sum1 = 0
sum2 = 0

f = open("ab.txt", "r")
for x in f:
    if x != "\n":
        temp += int(x)
    else:
        temp = 0
    if temp > sum:
        sum2 = sum1 
        sum1 = sum
        sum = temp
    elif temp > sum1:
        sum2 = sum1
        sum1 = temp
    elif temp > sum2:
        sum2 = temp

print(sum + sum1 + sum2)


