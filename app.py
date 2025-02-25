import requests
from datetime import datetime

def Weather_report(location):
    
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    key = "AZ94WHHAAH8V95MBDN63SU5DK"

    today = datetime.now().strftime("%Y-%m-%d")
    
    location_url = f"{base_url}/{location}/{today}/next2days?unitGroup=metric&key={key}" #Tengo que añadir el día de mañana e intentar conseguir el rango
    
    weather_data = requests.get(location_url).json()

    report = {
        "Localizacion": weather_data.get("address"),
        "Información": []
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
            "Fecha": date_format(),
            "Temp. media": round(day.get("temp"), 1),
            "Temp. maxima": round(day.get("tempmax"), 1),
            "Temp. minima": round(day.get("tempmin"), 1),
            "Precipitaciones": rain()
        }

        report["Información"].append(day_info)

    print(f"\nMeteorología en {report["Localizacion"]}:")
    for day in report["Información"]:
        print(f"Fecha: {day["Fecha"]}")
        print(f"Temp. media: {day["Temp. media"]}")
        print(f"Temp. maxima: {day["Temp. maxima"]}")
        print(f"Temp. minima: {day["Temp. minima"]}")
        print(f"Precipitaciones: {day["Precipitaciones"]}")


location = input("Escribe una ciudad: ").capitalize()
Weather_report(location)