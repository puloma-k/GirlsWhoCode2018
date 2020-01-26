# #create list of names
# fruit = ["banana", "apple", "watermelon", "cherries", "orange"]
#
# #randomly choose names
# from random import *
# randomIndex = randint(0, len(fruit) - 1)
#
# #print names
# print("Fruit:", fruit[randomIndex])




#create lists of sides, main courses, and desserts
sides = ["fries", "chips", "potatoes", "vegetables", "soup"]
main_course = ["pizza", "sushi", "pasta", "burger", "salad"]
dessert = ["ice cream", "cookie", "pie"]

#randomly choose names
from random import *
randomSide = randint(0, len(sides) - 1)
randomMainCourse = randint(0, len(main_course) - 1)
randomDessert = randint(0, len(dessert) - 1)

s = sides[randomSide]
m = main_course[randomMainCourse]
d = dessert[randomDessert]

#ask for which meals are wanted
side = True
while side == True:
    side = input("Would you like a side? ")
    if side == "yes":
        print(s)
        break
    elif side == "no":
        side == False
    else:
        print("Please answer yes or no")
        side == True

print(m)
print(d)






# #create lists of 3 and 5 syllable lines
# three_syllable = ["birds singing", "moonlight shine", "rainy dawn", "silent pond"]
# five_syllable = ["walking in the night", "a lovely sunset", "gentle drip of rain", "a lighting flash"]
#
# #randomly choose lines
# from random import *
# randomThree1 = randint(0, len(three_syllable) - 1)
# randomThree2 = randint(0, len(three_syllable) - 1)
# randomFive = randint(0, len(five_syllable) - 1)
#
# #print haiku
# print(three_syllable[randomThree1])
# print(five_syllable[randomFive])
# print(three_syllable[randomThree2])
