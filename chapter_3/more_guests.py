# oh look, more lists

guest_list = [] #empty
guest_list.append("Albert Einstein") #gosh this is annoying
guest_list.append("Marie Curie") 
guest_list.append("Carl Sagan") 
guest_list.append("Richard Feynman") #look at dat cliche

for i in range(len(guest_list)):
    message = "Dear " + guest_list[i].title() + ",\nYou have been invited to attend a dinner party at my home. Details to follow.\nRegards"
    print(message)

print("Wonderful news! We have a larger dinner table, and more people will be invited!")

guest_list.insert(0,"Madame Wu") #beginning
guest_list.insert(2,"Hedy Lamarr") #middle
guest_list.append("Lise Meitner") #end

for i in range(len(guest_list)):
    message = "Dear " + guest_list[i].title() + ",\nYou have been invited to attend a dinner party at my home. Details to follow.\nRegards"
    print(message)