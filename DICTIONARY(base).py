# creating a dictionary
a={"name":"james","age":"21","city":"london"}
print(type(a),a)
b=dict(name="james",age="21",city="london") 
print(b)
c={}
print(c)
# accessing items 
a={"name":"james","age":"21","city":"london"}
print(a["age"])
print(a.get("name"))
print(a.get("place"))
# changing
a={"name":"james","age":"21","city":"london"}
a["city"]="china"
print(a)
# adding
a["place"]="chi"
print(a)
# removing items 
a={"name":"james","age":"21","city":"london"}
b=a.pop("name")
print(b)
print(a)
a={"name":"james","age":"21","city":"london"}
c=a.popitem()
print(c)
a={"name":"james","age":"21","city":"london"}
del a["age"]
print(a)
a.clear()
print(a)
a={"name":"james","age":"21","city":"london"}
x=dict(a)
print(a)
# nested dictionary
v={"p1":{"name":"james","age":"21","city":"london"},
   "p2":{"name":"jake","age":"31","city":"mexico"},
   "p3":{"name":"jerry","age":"11","city":"america"}}
print(v["p2"]["age"])
# methods
a={"name":"james","age":"21","city":"london"}
print(a.keys())
print(a.values())
print(a.items())
a={"name":"james","age":"21","city":"london"}
a.update({"place":"mexico","age":22})
print(a)
keys=["name","age","city"]
n=dict.fromkeys(keys,"nil")
print(n)
a={"name":"james","age":"21","city":"london"}
z=a.setdefault("place","mexico")
print(z)
print(a)