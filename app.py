import requests
from datetime import datetime

def get_weather_data(location, days_range):

    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    key = "AZ94WHHAAH8V95MBDN63SU5DK"

    today = datetime.now().strftime("%Y-%m-%d")
    
    location_url = f"{base_url}/{location}/{today}/next{days_range}days?unitGroup=metric&key={key}" #Tengo que añadir el día de mañana e intentar conseguir el rango
    
    weather_data = requests.get(location_url).json()

    return weather_data

def format_data(weather_data):

    report = {
        "location": weather_data.get("address"),
        "information": []
    }

    for day in weather_data["days"]:

        def rain():
            if day.get("precipprob") > 0:
                return f"El porcentaje de probabilidad de precipitaciones es del {day.get("precipprob")}%"
            else:
                return "Sin precipitaciones."

        def date_format():

            date = day.get("datetime")
            return datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")

        day_info = {
            "date": date_format(),
            "Average temp.": round(day.get("temp"), 1),
            "Max temp.": round(day.get("tempmax"), 1),
            "Min temp.": round(day.get("tempmin"), 1),
            "Precipitation probability": rain()
        }

        report["information"].append(day_info)

    return report

def display_report(report):

    print(f"\nMeteorología en {report["location"]}:")
    for day in report["information"]:
        print(f"date: {day["date"]}")
        print(f"Average temp.: {day["Average temp."]}°C")
        print(f"Max temp.: {day["Max temp."]}°C")
        print(f"Min temp.: {day["Min temp."]}°C")
        print(f"Precipitation probability: {day["Precipitation probability"]}°C")

def main():

    location = input("Escribe una ciudad: ").capitalize()
    days_range = int(input("Rango de días de previsión: ")) - 1
    days_range_str = str(days_range)

    weather_data = get_weather_data(location, days_range_str)
    report = format_data(weather_data)
    display_report(report)

main()