import requests
'''
Assign a variable to URL to change it in future easier
'''
#url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f6cb1953-2034-4231-9e08-e81f8e65c8a7/dar1nrd-ecee77bd-3223-477a-a048-79f635ce12b3.jpg/v1/fill/w_800,h_534,q_75,strp/untitled_by_idabarracuda_dar1nrd-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTM0IiwicGF0aCI6IlwvZlwvZjZjYjE5NTMtMjAzNC00MjMxLTllMDgtZTgxZjhlNjVjOGE3XC9kYXIxbnJkLWVjZWU3N2JkLTMyMjMtNDc3YS1hMDQ4LTc5ZjYzNWNlMTJiMy5qcGciLCJ3aWR0aCI6Ijw9ODAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.4uGdEPxBePoR2BjRiq8nie7ZZuPEVwH0luNhJsiGEVk"

'''
Assign the response to a variable as well to work with it
'''
#response = requests.get(url)

'''
Status_code, e.g. 200 is success
'''
#print(response.status_code)

'''
.content or .text to view what you got. Can also do .content[:somenumber] to slice the string
'''
#print(response.content[:100])
#print(response.text)

'''
Proper way of opening a file. Saves it as a variable "file". 
Add e.g. writable binary - "wb")
'''
#with open("cool_image.png", "wb") as file: 
#    file.write(response.content)

'''
Practice. Adding If conditional in case file wasn't opened properly.
'''

#print("Gimme URL you bastard: ", end="")
#url = input()

#print("Gimme a name you bastard: ", end="")
#name = input()

#response = requests.get(url)

#if response.status_code == 200:
#    with open(name, "wb") as file:
#        file.write(response.content)
#        print("Done, wrote %d bytes" % len(response.content)) 
