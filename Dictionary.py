#dictionary = A changable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow",
            "russia":'Siberia'}

capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Las Vegas"})
#capitals.pop("China")
#capitals.clear()
#print(capitals['Russia'])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
print(capitals.items())

#for key,value in capitals.items():
#    print(key+ "'s capital is "+value)

x = input("Which country do you want to check?: ")

while x not in capitals:
    print("Data not found! You can update: ")
    y= input("Please add capital of " +x +": ")
    capitals.update({x:y})

for y in capitals.keys():
    if x == y:
        print(x+ "'s Capital is "+capitals.get(y))
    else:
        continue

print()