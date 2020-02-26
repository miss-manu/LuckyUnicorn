import random
from random import randint
import time
newline = "-----------------------------------"


# start of "enter" to start
enter = input("Press Enter To Start")
while enter != "":
    enter = input("Press Enter To Start\n")
# end of "enter" to start

# defining some values
token = ["zebra", "horse", "donkey", "unicorn"]
animal = random.choice(token)
cost = 1
depositMessage = "How much money would you like to deposit\n(Maximum 10 Dollars)"
# end of defining some values.

# start of Reservoir samples
#start of firstname sample
with open('./ReservoirFiles/firstname') as in_fd:
    firstname = next(in_fd) # fills array

    for i, line in enumerate(in_fd, start=1): # change this "1" to the line that it should start at?

        j = randint(0, i)
        if j == 0:
            firstname = line
#end of firstname sample


#start of age sample
with open('./ReservoirFiles/age') as in_fd:
    age = next(in_fd)

    for i, line in enumerate(in_fd, start=1):

        j = randint(0, i)
        if j == 0:
            firstname = line
#end of age sample

#start of gender sample
with open('./ReservoirFiles/gender') as in_fd:
    gender = next(in_fd)

    for i, line in enumerate(in_fd, start=1):

        j = randint(0, i)
        if j == 0:
            gender = line
#end of gender sample

#start of lastname sample
with open('./ReservoirFiles/lastname') as in_fd:
    lastname = next(in_fd)

    for i, line in enumerate(in_fd, start=1):

        j = randint(0, i)
        if j == 0:
            lastname = line
#end of lastname sample

#start of location sample
with open('./ReservoirFiles/location') as in_fd:
    location = next(in_fd)

    for i, line in enumerate(in_fd, start=1):

        j = randint(0, i)
        if j == 0:
            location = line
#end of location sample


# end of Reservoir samples


# start of character information

print("Character Information:")
print(newline)
print(age)
print(gender)
print(firstname)            # pretty much this is all temp, when I can be bothered I'll code a GUI in probably C++
print(lastname)
print(location)


# end of character information


# start of "deposit money thing"
print("How much money would you like to deposit into the machine?")
startingMoney = int(input(""))
while startingMoney > 10:
    print("You dont have %s in your wallet... You only have 10 dollars ;~;" %
          (startingMoney))
    startingMoney = int(input(""))
# end of "deposit money thing"


# start of if statments
if animal == "zebra":
    won = cost - .50
    balance = startingMoney + won
    print("Oh no! you just lost 50c, You rolled a %s, Your Balance is now $%s" % (animal, balance))

elif animal == "horse":
    won = cost - .50
    balance = startingMoney + won
    print("Oh no! you just lost 50c, You rolled a %s, Your Balance is now $%s" % (animal, balance))

elif animal == "donkey":
    won = 0 - cost
    balance = startingMoney + won
    print("Oh no! you just lost $1, You rolled a %s, Your Balance is now $%s" % (animal, balance))

elif animal == "unicorn":
    won = 5
    balance = startingMoney + won
    print("Congratulations You Won $%s, You rolled a %s, Your Balance is now $%s" % (won, animal, balance))

# end of if statments
