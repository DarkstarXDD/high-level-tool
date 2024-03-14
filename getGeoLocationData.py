import requests


class GeoLocationData:

    def __init__(self):
        response = requests.get("http://ip-api.com/json/?fields=16314363")
        data = response.json()

        formatted_data = {}

        for key, value in data.items():
            if value == "":
                formatted_data[key] = "-"
            else:
                formatted_data[key] = value

        self.public_ip = formatted_data["query"]
        self.continent = formatted_data["continent"]
        self.continent_code = formatted_data["continentCode"]
        self.country = formatted_data["country"]
        self.country_code = formatted_data["countryCode"]
        self.region_name = formatted_data["regionName"]
        self.city = formatted_data["city"]
        self.district = formatted_data["district"]
        self.zipcode = formatted_data["zip"]
        self.lat = formatted_data["lat"]
        self.lon = formatted_data["lon"]
        self.timezone = formatted_data["timezone"]
        self.currency = formatted_data["currency"]
        self.isp = formatted_data["isp"]
        self.org = formatted_data["org"]
        self.asn = formatted_data["as"]
        self.as_name = formatted_data["asname"]

        print("Request to the API endpoint was made")
