import requests


class GeoLocationData:

    def __init__(self):
        try:
            response = requests.get("http://ip-api.com/json/?fields=16314363")
            response.raise_for_status()  # Raises an exception for HTTP errors (e.g., 404, 500)
            data = response.json()

            formatted_data = {}

            # If the key value is an empty string, replace it with "-".
            for key, value in data.items():
                if value == "":
                    formatted_data[key] = "-"
                else:
                    formatted_data[key] = value

            # If the key itself is missing, use the default value of "-" for the attribute.
            self.public_ip = formatted_data.get("query", "-")
            self.continent = formatted_data.get("continent", "-")
            self.continent_code = formatted_data.get("continentCode", "-")
            self.country = formatted_data.get("country", "-")
            self.country_code = formatted_data.get("countryCode", "-")
            self.region_name = formatted_data.get("regionName", "-")
            self.city = formatted_data.get("city", "-")
            self.district = formatted_data.get("district", "-")
            self.zipcode = formatted_data.get("zip", "-")
            self.lat = formatted_data.get("lat", "-")
            self.lon = formatted_data.get("lon", "-")
            self.timezone = formatted_data.get("timezone", "-")
            self.currency = formatted_data.get("currency", "-")
            self.isp = formatted_data.get("isp", "-")
            self.org = formatted_data.get("org", "-")
            self.asn = formatted_data.get("as", "-")
            self.as_name = formatted_data.get("asname", "-")

            print("Request to the API endpoint was made")

        except requests.exceptions.RequestException as e:
            print("Error fetching data from API:", e)

            # Set default values for attributes in case of error
            self.public_ip = "-"
            self.continent = "-"
            self.continent_code = "-"
            self.country = "-"
            self.country_code = "-"
            self.region_name = "-"
            self.city = "-"
            self.district = "-"
            self.zipcode = "-"
            self.lat = "-"
            self.lon = "-"
            self.timezone = "-"
            self.currency = "-"
            self.isp = "-"
            self.org = "-"
            self.asn = "-"
            self.as_name = "-"
