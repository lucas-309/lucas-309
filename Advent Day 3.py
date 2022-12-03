# Part 1
sum = 0
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
temp1 = ""
temp2 = ""
f = open("3.txt", "r")
for x in f:
    
    temp1 = x[0:int((len(x)-1)/2)]
    temp2 = x[int((len(x)-1)/2):int(len(x))]
    print(temp1, temp2)
    
    for i in range(len(temp1)):
        for j in range(len(temp2)):
            if temp1[i] == temp2[j]:
                sum += letters.index(temp1[i]) + 1
                break
        else:
            continue
        break
        

print(sum)
