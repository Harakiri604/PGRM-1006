import requests 
'''
url = "https://api.exchangeratesapi.io/latest?base=CAD"
response = requests.get(url).json()

userRate=input("Which rate do you want: ")
print(response["rates"][rates])
'''

'''
url = "https://api.exchangeratesapi.io/latest?"

base=input("What currency should we base on: ")
symbols=input("What currencies should we check: ")

url = url + "base=" + base.upper() \
+ "&" + "symbols=" + symbols.upper()

response=requests.get(url)
json=response.json()
print(json)
'''

'''
url = "https://api.exchangeratesapi.io/latest"

base=input("What currency should we base on: ")
symbols=input("What currencies should we check: ")

params={'base':base.upper(),
        'symbols':symbols.upper()}

response=requests.get(url, params=params)
json=response.json()
print(json)
'''

