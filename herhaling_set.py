lotto = {3,16,7,42,28,19,33,30,23,12}
for cijfer in lotto:
    print(cijfer,end=" ")
print()

munten = {"euro","gulden","euro","dollar","yenn","pound","dollar"}
print(munten,len(munten))
munten.add("BEF")
print(munten)
munten.remove("euro")
print(munten)
munten.pop()
print(munten)