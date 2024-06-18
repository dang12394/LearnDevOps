#tuple = collection which is ordered and unchangeable
#        used to group together related data

student = ("Dang",29,"male",)

print(student.count("Dang"))
print(student.index("male"))

for x in student:
    print(x)

if "Dang" in student:
    print("Dang is here!")