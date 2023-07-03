#list datastructure, it is ordered and changeable
cars = ["Mercedes", "Nissan", "Toyota", "Range"]
cars[1] = "Subaru"
cars.append("Mistubishi")
cars.insert(2,"Bmw")
cars.pop(4)
cars.sort()
print(cars)
# this is a tuple,ordered,its unchangeable
fruits = ("Mango", "Orange", "Pineapple", "Avocado", "lemon", "Kiwi")

print(fruits)
for f in fruits:
    print(f)

# sets datastructure,unordered
countries = {"Kenya", "Egypt", "Nigeria", "South Africa", "Cameroon"}
print(countries)

#dictionaries
matunda = {
    "amount":40,
    "jina":"Ndizi",
    "rangi":"Yellow",
    "taste":"Sweet"
}
matunda["size"] = "Medium"
matunda.pop("rangi")
print(matunda)