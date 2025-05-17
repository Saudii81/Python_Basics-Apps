import random

randValue = str(random.randrange(1,21))
print(random.randrange(1,21))

txts = str(input("Guess the Random Nuumber: "))

#if (txts == randValue):
#    print("Correct!!!")

#elif (txts <= randValue)
#    print("Less Value")

#else (txts >= randvalue)
#     print("Too High")

#i = 1
#while i < 21:
#    print(i)

#   i+=i

while (txts < randValue):
    print("Less Value, try again")
    txts = input("Guess the Random Nuumber: ")

while (txts > randValue):
    print("Too High, try again")
    txts = input("Guess the Random Number: ")

if (txts == randValue):
    print("Correct!!!")
