from sys import argv
k = argv[1:]
n1 = int(k[0])
n2 = int(k[1])
if(n1>n2):
    greater = n1
else:
    greater = n2

while(1):
    if((greater % n1 == 0) and (greater % n2 == 0)):
        l = greater
        break
    greater += 1

print(l)