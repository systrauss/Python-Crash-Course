# oh look, more lists

guest_list = [] #empty
guest_list.append("Albert Einstein") #gosh this is annoying
guest_list.append("Marie Curie") 
guest_list.append("Carl Sagan") 
guest_list.append("Richard Feynman") #look at dat cliche

for i in range(len(guest_list)):
    message = "Dear " + guest_list[i].title() + ",\nYou have been invited to attend a dinner party at my home. Details to follow.\nRegards"
    print(message)

print("Sadly, " + guest_list[2].title() + " cannot make it.")

guest_list[2] = "Madame Wu" # replacing the guest

print("We are instead, extending an invitation to " + guest_list[2].title() + ".")

for i in range(len(guest_list)):
    message = "Dear " + guest_list[i].title() + ",\nYou have been invited to attend a dinner party at my home. Details to follow.\nRegards"
    print(message)