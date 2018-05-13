#more lists. apparently, i used loops earlier than expected.

pizzas = ['cheese','hawaiian','sausage','mushroom']

for pizza in pizzas:
    #print(pizza)
    message = "I like " + pizza + " pizza."
    print(message)

message = "Pizza is really a guilty pleasure!"
print(message)

friend_pizzas = pizzas[:]
pizzas.append('bacon')
friend_pizzas.append('pepperoni')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)