import random

#dimY = int(input("Dimentions : ")) TODO Get monitor dimentions and use them for this
dimY = 55
dimX = int(dimY * 3)
print(dimX)
playerY = random.randint(1,dimY - 1)
print(dimY)
print("#" + ("-"*dimX) + "#")
for i in range(1,dimY):
    print("|" + " "*dimX + "|")
    if(i == playerY):
        print("Player Y is Here")
print("#" + ("-"*dimX) + "#")
