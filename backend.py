import requests

api_key = "c69562261a70c34716be62374f16688a"


def get_data(place, forcast_days=1):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    num_days = 8 * forcast_days
#    data["list"]["main"]["real_temp"] = data["list"]["main"]["temp"] / 10
    filtered_data = data["list"]
    filtered_data = filtered_data[:num_days]
    return filtered_data


if __name__ == "__main__":
    porpose = get_data(place="tirsg", forcast_days=4)
    print(porpose)
