import requests
import os

url = "https://api.github.com/emojis"

response = requests.get(url)
json = response.json()

#Get keys+values = .items / keys = .keys / values = .values
print(list(json.items())[:10])

#Import OS (above) and make directory first
'''
os.makedirs("emojis", exist_ok=True)

json_len = len(json)
index = 1
if response.status_code == 200:
    print("\nRequest successful, downloading images...\n")
    for emoji_name, emoji_url in json.items():
        print("%d/%d Downloading: %s" % (index, json_len, emoji_name))
        pic = requests.get(emoji_url)
        with open("emojis\\{}).png".format(emoji_name), "wb") as file:
            file.write(pic.content)
            index+=1
    print("Done.")
'''