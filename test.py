import requests

response = requests.get("http://ip-api.com/json")
# print(response)

data = response.json()
# print(data)

country = data["country"]
country_code = data["countryCode"]
province = data["regionName"]
city = data["city"]
zipcode = data["zip"]
timezone = data["timezone"]

print(country)
print(country_code)
print(province)
print(city)
print(zipcode)
print(timezone)
