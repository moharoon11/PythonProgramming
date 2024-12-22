from urllib import request

r = request.urlopen("http://www.google.com")
print(r.getcode())
print(r.read())

# shooting request to my own api
portfolioResponse = request.urlopen("http://13.233.158.50/users/get")
print(portfolioResponse.getcode())
print(portfolioResponse.read())