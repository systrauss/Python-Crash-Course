# oh look, more lists

guest_list = [] #empty
guest_list.append("Albert Einstein") #gosh this is annoying
guest_list.append("Marie Curie") 
guest_list.append("Carl Sagan") 
guest_list.append("Richard Feynman") #look at dat cliche

for i in range(len(guest_list)):
    message = "Dear " + guest_list[i].title() + ",\nYou have been invited to attend a dinner party at my home. Details to follow.\nRegards"
    print(message)

print("\nWonderful news! We have a larger dinner table, and more people will be invited!\n")

guest_list.insert(0,"Madame Wu") #beginning
guest_list.insert(2,"Hedy Lamarr") #middle
guest_list.append("Lise Meitner") #end

for i in range(len(guest_list)):
    message = "Dear " + guest_list[i].title() + ",\nYou have been invited to attend a dinner party at my home. Details to follow.\nRegards"
    print(message)

print("\nTerrible news! The table will not arrive in time. I can only choose two of you for the dinner party!\n")

for i in range(len(guest_list)-2):
    uninvited = guest_list.pop(1)
    message = "Dear " + uninvited + ",\nRegretfully, I can no longer invite you to dinner. Hopefully we can do this again in the future.\nRegards"
    print(message)

for i in range(len(guest_list)):
    message = "Dear " + guest_list[i].title() + ",\nYou are still invited. Details to follow.\nRegards"
    print(message)

for i in range(len(guest_list)):
    del guest_list[0]

print(guest_list)