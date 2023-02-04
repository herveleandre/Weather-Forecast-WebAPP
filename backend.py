import requests

API_KEY = "9c644e18caff1a53a61b491dffd73f39"


def get_data(place, days=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    request = requests.get(url)
    data = request.json()
    filter_data = data["list"]
    nr_values = 8 * days
    filter_data = filter_data[:nr_values]

    return filter_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=3))
