# map() =   applies a function to each item in an iterable(list, tuple,etc.)
#
# map(function, iterable

store =[("Shirt", 20.00),
        ("pants",25.00),
        ("jacket",50.00),
        ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = map(to_euros,store)
store_dollar = map(to_dollars,store)
for i in store_euros:
    print(i)

for j in store_dollar:
    print(j)