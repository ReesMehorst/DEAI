from random import randrange
lijst = []

for i in range(20):
    lijst.append(randrange(100))


for item in lijst:
    print(item)

for item in lijst:
    if((item % 2) == 0):
        [print(item)]