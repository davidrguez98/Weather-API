from backend.weather_functions import *

def main(): #Se pide la localización y el rango de días. Ejecuta el programa

    try:
        location = input("Escribe una ciudad: ").capitalize()
    except ValueError:
        print("Error: Escribe un nombre de ciudad válida.")
        return
    
    try:
        days_range = int(input("Rango de días de previsión: ")) - 1
        if days_range <= 0:
            print("Error: El rango de días debe de ser positivo")
            return
        else:
            days_range_str = str(days_range)
    except ValueError:
        print("Error: Escribe un número válido de días.")
        return

    weather_data = get_weather_data(location, days_range_str)

    if weather_data is None:
        print("Error: No se pudo obtener información sobre el clima.")
        return

    report = format_data(weather_data)
    display_report(report)

main()