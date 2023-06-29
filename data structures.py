# list datastructure
# a list enables you to change the data
myclassmate = ["Erick", "joan", "daniel", "susan", "purity"]
mynos = [4, 9, 20, 3, 1, 50, -9]
myclassmate[0] = "Daniel"
mynos.sort()
myclassmate.append("christine")
myclassmate.insert(2, "Michael")
myclassmate.pop(0)
print(myclassmate)
print(mynos)
for jina in myclassmate:
    print(jina)
for nambari in mynos:
    print(nambari)

# This is a tuple
countries = ("Kenya", "Uganda", "Tanzania", "Burundi")
print(countries)
for nchi in countries:
    print(nchi)

# a set/sets

cars = {"Toyota", "Nissan", "Mercedes", "Subaru", "Rangerover"}
print(cars)
for magari in cars:
    print(magari)

# a dictionary data structures

matunda = {
    "price": 50,
    "color": "green",
    "name": "Mangoes",
    "origin": "Kitui",
    "Type": "carabao"
}

matunda["shape"] = "oval"
for fruits in matunda:
    print(fruits)
bei = matunda["price"]
print(bei)
rangi = matunda["color"]
print(rangi)
jina = matunda["name"]
print(jina)
place = matunda["origin"]
print(place)
ila = matunda["Type"]
print(ila)
umbo = matunda["shape"]
print(umbo)
