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


