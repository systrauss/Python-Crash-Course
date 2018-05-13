# playing with tuples! aka immutable lists

buffet_foods = ('rice','beans','chicken','salsa','queso')

print("Original menu:")
for food in buffet_foods:
    print(food)

#sends up error because tuple cannot change
#buffet_foods[1] = 'pico de gallo'

print("New menu:")
buffet_foods = ('rice','beans','steak','pico de gallo','queso')
for food in buffet_foods:
    print(food)