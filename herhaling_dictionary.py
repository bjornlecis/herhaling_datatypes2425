"""namen = {"p1":"Jan","p2":"Piet","p3":"Joris","p4":"Corneel"}
for k,v in namen.items():
    print(k,v)

namen["p5"] = "Jef"
namen.pop("p2")
for naam in namen.values():
    print(naam)"""

personen = {
    "p1":{"naam":"jan","leeftijd":30},
    "p2":{"naam":"pier","leeftijd":25},
    "p3":{"naam":"jan","leeftijd":32}
}
print("naam","leeftijd")
for persoon,data in personen.items():
    for item in data.values():
        print(item,end="\t")
    print("")

