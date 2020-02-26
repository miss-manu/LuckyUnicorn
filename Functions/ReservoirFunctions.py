"""
----------------------
Creator : Pluto
Last Edited : 26/2/2020
Usage : Cleans Up Main File, Pretty much just a dump of functions
License : www.gnu.org/licenses/lgpl-3.0.txt
Repository : https://github.com/PlvtoV2/LuckyUnicorn/blob/master/LuckyUnicorn.py
----------------------
"""

from random import randint
def lastname():
 with open('./ReservoirFiles/lastname') as in_fd:
     lastname = next(in_fd)

     for i, line in enumerate(in_fd, start=1):

         j = randint(0, i)
         if j == 0:
             lastname = line
 print("Lastname: %s" % (lastname))

def firstname():
 with open('./ReservoirFiles/firstname') as in_fd:
     firstname = next(in_fd)

     for i, line in enumerate(in_fd, start=10):

         j = randint(0, i)
         if j == 0:
             firstname = line
 print("Firstname: %s" % (firstname))

def age():
 with open('./ReservoirFiles/age') as in_fd:
     age = next(in_fd)

     for i, line in enumerate(in_fd, start=14):

         j = randint(0, i)
         if j == 0:
             age = line
 print("Age: %s" % (age))

def location():
 with open('./ReservoirFiles/location') as in_fd:
     location = next(in_fd)

     for i, line in enumerate(in_fd, start=1):

         j = randint(0, i)
         if j == 0:
             location = line
 print("Lives In: %s" % (location))

def gender():
 with open('./ReservoirFiles/gender') as in_fd:
     gender = next(in_fd)
     for i, line in enumerate(in_fd, start=10):
         j = randint(0, i)
         if j == 0:
             gender = line
 print("Gender: %s" % (gender))

