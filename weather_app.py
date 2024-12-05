import requests

# OpenWeatherMap API key (replace with your own key)
API_KEY = "98385f0b6a49c8c9d7ec7dc7d4f41a7f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(location, temperature_unit_selection):
    try:
        # Prepare the API request
        if temperature_unit_selection == "c":
            params = {
                "q": location,
                "appid": API_KEY,
                "units": "metric"  # Celsius
            }
        else:
            params = {
                "q": location,
                "appid": API_KEY,
                "units": "imperial"  # Fahrenheit
            }
  
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Parse the response JSON
        weather_data = response.json()

        # Extract relevant information
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        condition = weather_data["weather"][0]["description"]

        # Display weather information
        temp_unit = "°C" if temperature_unit_selection == "c" else "°F"
        print(f"\nWeather in {city}, {country}:")
        print(f"- Condition: {condition.capitalize()}")
        print(f"- Temperature: {temperature}{temp_unit}")
        print(f"- Humidity: {humidity}%\n")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Could not retrieve weather data. Please check the location name or API key.")

# Main Program
print("Welcome to the Weather App!")
while True:
    
    #selecting user choice unit.
    temperature_unit_selection = input("Select the units (c for Celsius, f for Fahrenheit): ").strip().lower()
    if temperature_unit_selection.lower() not in ["c", "f"]:
        print("Invalid unit selection. Please use 'c' for Celsius or 'f' for Fahrenheit.")
        continue

    # Select weather user want city name or zip code.
    search_type = input("Do you want to search by (city press c , for Zip code press z): ").strip().lower()
    if search_type not in ["c","z"]:
        print("Invalid search type. Please type 'city' or 'zip'.")
        continue    
    elif search_type == "c":
        location = input("Enter the City Name: ").strip()
    else:
        location = int(input("Enter the ZIP Code: "))

    get_weather(location, temperature_unit_selection)
    
    # Ask the user if they want to calculate again 
    again = input("Do you want to search another city? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break