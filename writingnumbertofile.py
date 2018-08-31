import random
f = open("songuyen.txt", "w")
for count in range(10):
    number = random.randint(1,10)
    f.write(str(number) + '\n')
f.close()
