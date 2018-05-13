# editing a code in the book

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
#print(my_foods)
for food in my_foods:
    print(food)

print("My friend's favorite foods are:")
#print(my_foods)
for food in friend_foods:
    print(food)