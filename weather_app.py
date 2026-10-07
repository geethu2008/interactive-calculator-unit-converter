import requests


API_KEY = "YOUR_OPENWEATHER_API_KEY"


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404:
            print("City not found.")
            return

        response.raise_for_status()

        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n==============================")
        print("       WEATHER REPORT")
        print("==============================")
        print(f"City        : {city_name}, {country}")
        print(f"Temperature : {temperature} °C")
        print(f"Feels Like  : {feels_like} °C")
        print(f"Humidity    : {humidity}%")
        print(f"Weather     : {description}")
        print(f"Wind Speed  : {wind_speed} m/s")
        print("==============================")

    except requests.exceptions.RequestException as e:
        print("Error connecting to weather service.")
        print(e)

    except KeyError:
        print("Unexpected response from the weather API.")


def main():
    print("===== WEATHER APP =====")

    while True:
        city = input("\nEnter city name (or type 'exit'): ")

        if city.lower() == "exit":
            print("Thank you for using Weather App!")
            break

        if city.strip() == "":
            print("Please enter a city name.")
            continue

        get_weather(city)


main()