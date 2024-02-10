from datetime import datetime

from entities import AirLine
from entities import Client
from entities import Package

if __name__ == '__main__':
    menu = "Opciones del Sistema: \n" \
           "1 - Transportar paquete \n" \
           "2 - Obtener Reporte completo\n" \
           "3 - Obtener Reporte por Fecha\n" \
           "4 - Salir"

    air_line = AirLine()
    print(menu)
    option = input("Seleccione una Opción\n")
    while option != "4":
        if option == "1":
            client_name = input("Ingrese el nombre del cliente\n")
            transported_date = input("Ingrese la fecha de Transporte (Formato YYYY-MM-dd)\n")

            transported_date_formatted = datetime.strptime(transported_date, "%Y-%m-%d")

            client_1 = Client(client_name)
            package = Package(client_1, transported_date_formatted)

            response = air_line.transport_package(package)

        elif option == "2":
            response = air_line.generate_report()

        elif option == "3":
            filter_date = input("Ingrese la fecha (Formato YYYY-MM-dd)\n")

            formatted_filter_date = datetime.strptime(filter_date, "%Y-%m-%d")
            response = air_line.generate_report(formatted_filter_date)
        else:
            response = "Opción Incorrecta, vuelva a intentar.\n"

        print(response)

        print(menu)
        option = input("Seleccione una Opción\n")
