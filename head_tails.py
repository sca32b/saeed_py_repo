import random
heads=0
tails=0
cointoss=[]

for i in range(10):
 randomnum = random.randint(0,1)
 if randomnum == 0:
     heads += 1
     cointoss.append("Heads")
 else:
     tails += 1
     cointoss.append("Tails")

print(f"The number of heads is {heads} and the number of tails is {tails}")
print("The last element is " + cointoss[-1])