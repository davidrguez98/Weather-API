import requests
from datetime import datetime

def Weather_report(location):
    
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    key = "AZ94WHHAAH8V95MBDN63SU5DK"

    today = datetime.now().strftime("%Y-%m-%d")
    tomorrow = "tomorrow"
    value_days = "next{value}days"
    
    location_url = f"{base_url}/{location}/{today}?unitGroup=metric&key={key}" #Tengo que añadir el día de mañana e intentar conseguir el rango
    
    weather_data = requests.get(location_url).json()

    report = {
        "Localización": weather_data.get("address"),
        "Información": []
    }

    for day in weather_data["days"]:

        def rain():
            if day.get("precipprob") > 0:
                return f"Hoy lloverá. El porcentaje de probabilidad es del {day.get("precipprob")}"
            else:
                return "Hoy no lloverá."

        def date_format():

            date = day.get("datetime")
            return datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")

        day_info = {
            "Fecha": date_format(),
            "Temp. media": round(day.get("temp"), 1),
            "Temp. maxima": round(day.get("tempmax"), 1),
            "Temp. minima": round(day.get("tempmin"), 1),
            "Precipitaciones": rain()
            
        }

    print(f"Meteorología de hoy en {location}:")
    print(f"Temp. media: {day_info["Temp. media"]} °C")
    print(f"Temp. máxima: {day_info["Temp. maxima"]} °C")
    print(f"Temp. mínima: {day_info["Temp. minima"]} °C")
    print(rain())

location = input("Escribe una ciudad: ").capitalize()
Weather_report(location)