def leap_year():
    Año = int(input("Ingrese un año: "))

    if (Año % 400 == 0) or (Año % 4 == 0 and Año % 100 != 0):
        print(f"El año {Año} es bisiesto")
    else:
        print(f"El año {Año} no es bisiesto")
