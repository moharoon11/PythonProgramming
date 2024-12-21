person = {
    "name" : "Mohamed Haroon",
    "age" : 21.7,
    "frontend_skill" : {"html", "css", "js", "react"},
    "backend_skill" : {"Java", "Python", "J2EE", "Hibernate", "Spring Boot", "etc"},
    "favourite_sports" : ["Football", "Settle Cork"],
}

print(person)
print(type(person))
print(person['name'])
print(person.get('backend_skill'))
# person.clear()
person["age"] = 21
print(person)

print(person.get("favourite_sports").append("Kabadi"))
print(person)

print(person.keys())
print(person.values())
print(person.items())