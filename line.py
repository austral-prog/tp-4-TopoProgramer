import math
def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    Cuenta1 = (A * X1) + B #Y1
    Cuenta2 = (A * X2) + B #Y2
    Cuenta3 = X2 - X1 
    Cuenta4 = Cuenta2 - Cuenta1
    Cuenta5 = math.pow(Cuenta4,2)
    Cuenta6 = math.pow(Cuenta3,2)
    Cuenta7 = Cuenta6 + Cuenta5
    Cuenta8 = math.sqrt(Cuenta7)
    print("El coeficiente A de su ecuación de la recta es:",A)
    print("El coeficiente B de su ecuación de la recta es:",B)
    print("El coeficiente X1 de su ecuación de la recta es:",X1)
    print("El coeficiente X2 de su ecuación de la recta es:",X2)
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {A}X + {B}")
    print("")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Cuenta1})")
    print(f"\tP2 ({X2}, {Cuenta2})")
    print("")
    print(f"La distancia entre ellos es: {Cuenta8}")
