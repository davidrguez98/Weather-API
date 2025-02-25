import requests
from requests.exceptions import RequestException
from datetime import datetime

def get_weather_data(location, days_range): #Se conecta a la API y devolver los datos JSON
    
        base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
        key = "AZ94WHHAAH8V95MBDN63SU5DK"

        today = datetime.now().strftime("%Y-%m-%d")
        
        location_url = f"{base_url}/{location}/{today}/next{days_range}days?unitGroup=metric&key={key}"

        try:    
            weather_data = requests.get(location_url).json()
            return weather_data
        
        except RequestException:
            
            print("Error: No se pudo conectar con el servidor. Verifica tu conexión a internet.")
            return None

def format_data(weather_data): #Transforma en un diccionario el JSON

    report = {
        "location": weather_data.get("resolvedAddress"),
        "information": []
    }

    for day in weather_data["days"]:

        def rain():
            if day.get("precipprob") > 0:
                return f"The probability of precipitation is {day.get("precipprob")}%"
            else:
                return "No precipitation"

        def date_format():

            date = day.get("datetime")
            return datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")

        day_info = {
            "Date": date_format(),
            "Average temp.": round(day.get("temp"), 1),
            "Max temp.": round(day.get("tempmax"), 1),
            "Min temp.": round(day.get("tempmin"), 1),
            "Precipitation probability": rain()
        }

        report["information"].append(day_info)

    return report

def display_report(report): #Imprime el informe meteorológico

    print(f"\nMETEOROLOGY IN {report["location"].upper()}:")
    for day in report["information"]:
        print(f"Date: {day["Date"]}")
        print(f"Average temp.: {day["Average temp."]}°C")
        print(f"Max temp.: {day["Max temp."]}°C")
        print(f"Min temp.: {day["Min temp."]}°C")
        print(f"Precipitation probability: {day["Precipitation probability"]}\n")
