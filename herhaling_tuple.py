def voeg_naam_toe(tuple_user,item):
    tuple_user = list(tuple_user)
    tuple_user.append(item)
    return tuple(tuple_user)
def verwijder_naam(tuple_user,item):
    if isinstance(tuple_user,tuple):
        tuple_user = list(tuple_user)
        if item in tuple_user:
            tuple_user.remove(item)
            return tuple(tuple_user)
        else:
            print("naam in in de tuple")
    else:
        print("geen tuple meegeven")


namen = ("jan","piet","joris","corneel")
namen2 = ["jan","piet","joris","corneel"]
namen2.append(["a","b","c"])
print(len(namen2))
a,b,c = namen2[-1]
print(a,b,c)
namen2[3] = voeg_naam_toe(namen,"jef")
print(namen2)
for naam in namen:
    print(naam)
namen = voeg_naam_toe(namen,"jef")
print(namen)
print(type(namen))
namen = verwijder_naam(namen,"piet")
print(namen)
t1 = (2,5,8,9)
t2 = (9,7,6,2)
t3 = t1+t2
print(t3)
tuple1 = (2, 5, 4,2)
tuple2 = (3, 0, 2,7)

# Gebruik zip() en een list comprehension
result = tuple(a + b for a, b in zip(tuple1, tuple2))
print(result)
