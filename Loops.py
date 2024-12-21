numbers = [1,2,3,4,5,6,7]

for num in numbers:
    print(num)

namesSet = {"mohamed haroon", "Mohamed Haroon", "mohamed haroon", "Haroon", "Haroon"}

for name in namesSet:
    print(name)

person = {
    "name" : "Mohamed Haroon",
    "age" : 21.7,
    "frontend_skill" : {"html", "css", "js", "react"},
    "backend_skill" : {"Java", "Python", "J2EE", "Hibernate", "Spring Boot", "etc"},
    "favourite_sports" : ["Football", "Settle Cork"],
}

for key in person:
    print(f"key = {key} -> value = {person.get(key)}")

for key in person:
    print(f"key = {key} -> value = {person[key]}")


for key in person.keys():
    print(f"Key = {key}")

for value in person.values():
    print(f"value = {value}")

for key, value in person.items():
    print(f"key = {key} -> value = {value}")

