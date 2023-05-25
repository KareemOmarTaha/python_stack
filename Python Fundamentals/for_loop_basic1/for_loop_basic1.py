for x in range (150):
    print(x)

for y in range (5 , 1000 , 5):
    print(y)

z = 0
while z < 100:
    z += 1 
    if z % 5 == 0 :
        print("coding")
    if z % 10 == 0:
        print("coding Dojo")
    else:
        print(z)

w = 0
k = 0
while w < 500000:
    w += 1 
    if w % 2 != 0:
        k = k + w
print(k)


for fours in range (2018 , 0 , -4):
    print(fours)


lowNum = 0
highNum = 50
mult = 5
for multNum in range (lowNum , highNum+1):
    if multNum % mult == 0:
        print(multNum)