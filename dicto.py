mydict = {
    "Tom holland":"Spider Man",
    "Tiger":"Animal",
    "Lalit":"Boy",
    "color":["Black","Red","Blue","Pink"],
    "tutp":("myTuple",89),
    "Bool":True
}


print(type(mydict))
print(mydict["Tiger"])

print(len(mydict))

get()

x = mydict.get("Tiger")
print(x)

mydict["Tom holland"] = "actor"

mydict.update({"Tom holland":"Actor"})



mydict["flowers"] = "rose"

print(mydict)

thisdict = mydict.copy()


print(thisdict)


myfamliy = {
    "child 1":{
        "name" : "EMily",
        "years": 12,
    },
    "child 2":{
        "name" : "Maddy",
        "years": 10,
    }
}


print(myfamliy)
