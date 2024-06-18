#slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

##indexing[]
name = 'Nhat Dang'

first_name = name[:4] #name[0:4]
last_name = name[5:] #name[5:10]
funky_name = name[::2] #name[0:10:2]
reversed_name = name[::-1]
print(first_name +' '+ last_name)
print(funky_name)
print(reversed_name)

##slice()

website1 = 'https://mantu.com'
website2 = 'https://amaris.com'
slice = slice(8,-4)

print(website1[slice].capitalize())
print(website2[slice].capitalize())
