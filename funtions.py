#write function which takes three arguments from user
#city , country, continent, and displays the following output:
def location(city,country,continent):
         print(city, "is a city that is located in", country, "which is in",continent)
city,country,continent=map(str,input().split())
location(city,country,continent)
