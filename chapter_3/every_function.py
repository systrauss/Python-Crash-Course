#just find a way to use every function dammit

rivers = []
rivers.append("nile")
rivers.append("mississippi")
rivers.insert(0,"snake")
rivers.insert(1,"severn")

print(rivers)
message = "The " + rivers[0].title() + " and " + rivers[3].title() + " are in the US."
print(message)
print(sorted(rivers))
not_us = rivers.pop(2)
message = "The " + not_us.title() + " is in Egypt."
print(message)
rivers.sort()
print(rivers)
rivers.remove('severn')
print(rivers)
