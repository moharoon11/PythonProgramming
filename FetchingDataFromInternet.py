from urllib import request
import json
import pyttsx3

r = request.urlopen("http://www.google.com")
print(r.getcode())
print(r.read())

# shooting request to my own api
portfolioResponse = request.urlopen("http://13.233.158.50/users/get")
print(portfolioResponse.getcode())
print(portfolioResponse.read())


# getting random jokes from jokes api

randomJokes = request.urlopen("http://official-joke-api.appspot.com/random_ten")

print(randomJokes.getcode())
data = randomJokes.read()
jsonData = json.loads(data)


class Jokes :

       def __init__(self, id, type, setup, punchline) :
           self.id = id
           self.type = type
           self.setup = setup
           self.punchline = punchline


       def __str__(self):
           return f"id = {self.id}, type = {self.type}, setup = {self.setup}, " \
                  f"punchline = {self.punchline}"


listOfJokes = []

for j in jsonData:
    joke = Jokes(j["id"], j["type"], j["setup"], j["punchline"])
    listOfJokes.append(joke)

for joke in listOfJokes:
    pyttsx3.speak("setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("punchline")
    pyttsx3.speak(joke.punchline)


