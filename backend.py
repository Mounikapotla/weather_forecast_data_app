import requests

API_KEY = "02610c73c0d8bd7acb643fbbf2db7bc9"
def get_data(place, forecast_days=None):
     url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
     response = requests.get(url)
     data = response.json()
     filtered_data = data["list"]
     nr_values = 8 * forecast_days
     filtered_data = filtered_data[:nr_values]
     return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days =3))








