#Import the relevant library
import requests

#Define the base URL
base_url = "https://api.github.com/search/repositories"

#Tell the user what is up
print("This programs shows the description of the top 10 repositories on GitHub based on your search query")

#Get user input and convert it into appropriate format for concatenation
query_term = input("Please enter your search query: ")
query = "?q=" + query_term

language_choice = int(input("Please select the language option - 1 for Python or 2 for Java: "))
if (language_choice == 1):
    language = "+language:python"
elif (language_choice == 2):
    language = "+language:java"

#Build the query
url = base_url + query + language + "&sort=stars&order=desc"

#Get the response and convert it into JSON
response = requests.get(url)
json = response.json()

#Create a loop with a counter that iterates through JSON key "items"
#and shows the value of the key "description" within each of the "items"
counter = 0
repository = 0
for results in json["items"]:
    if (counter<10):
        print("Repository", repository, "- ", end="")
        print (results["description"])
        counter+=1
        repository+=1
    else:
        break