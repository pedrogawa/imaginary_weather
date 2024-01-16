import random
from typing import List, TypedDict

class WeatherData(TypedDict):
    day: int
    temperature: int
    humidity: str

def generate_weather_data(num_days: int) -> List[WeatherData]:
  weather_data_aux: List[WeatherData] = []
  for x in range(num_days):
    weather_data_aux.append({'day': x+1, 'temperature': random.randint(20, 40), 'humidity': str(random.randint(30, 90)) + '%'})

  return weather_data_aux

def filter_data(weather_data: List[WeatherData], temp_threshold: int):
  data_aux: List[WeatherData] = []
  for weather in weather_data:
    if (weather['temperature'] >= temp_threshold):
      data_aux.append(weather)

  return data_aux

def calculate_average_humidity(weather_data: List[WeatherData]) -> int:
  humidity_values = map(lambda record: int(record['humidity'].rstrip('%')), weather_data)
  average_humidity = sum(humidity_values) / len(weather_data)

  return average_humidity

def sort_data_by_temperature(weather_data: List[WeatherData], isAscending: bool) -> List[WeatherData]:
  sorted_data_ascending = sorted(weather_data, key=lambda x: x['temperature'])
  sorted_data_descending = sorted(weather_data, key=lambda x: x['temperature'], reverse=True)

  if (isAscending):
    return sorted_data_ascending
  else:
    return sorted_data_descending


def main():
    weather_data: List[WeatherData] = []
    data_generated = False

    while True:
        print("\nOptions:")
        print("1. Generate Weather Data")
        print("2. Filter Data")
        print("3. Calculate Average Humidity")
        print("4. Sort Data by Temperature")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            num_days = input("Enter the number of days to generate data for: ")
            if num_days.isdigit():
                weather_data = generate_weather_data(int(num_days))
                data_generated = True
                print("Weather data generated.")
            else:
                print("Invalid input. Please enter a number.")

        elif choice in ['2', '3', '4']:
            if not data_generated:
                print("Please generate weather data first.")
                continue

            if choice == '2':
                temp_threshold = input("Enter temperature threshold: ")
                if temp_threshold.isdigit():
                    filtered_data = filter_data(weather_data, int(temp_threshold))
                    print("Filtered data:", filtered_data)
                else:
                    print("Invalid input. Please enter a number.")

            elif choice == '3':
                average_humidity = calculate_average_humidity(weather_data)
                print(f"Average Humidity: {average_humidity}%")

            elif choice == '4':
                order = input("Sort in ascending order? (yes/no): ").lower()
                if order in ['yes', 'no']:
                    isAscending = order == 'yes'
                    sorted_data = sort_data_by_temperature(weather_data, isAscending)
                    print("Sorted data:", sorted_data)
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()