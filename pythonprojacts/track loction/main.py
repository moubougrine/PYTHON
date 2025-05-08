import requests

access_key = '925827276741c9e4904d25e75f35b043'
phone_number = '+212606642110'

url = f'http://apilayer.net/api/validate?access_key={access_key}&number={phone_number}'

response = requests.get(url)
data = response.json()

# طباعة النتائج
print("Number:", data['number'])
print("Country  :", data['country_name'])
print("type of number:", data['line_type'])
