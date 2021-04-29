import math

tasa_de_natalidad = float(17.16) #float(input("Tasa de Natalidad: "))
tasa_de_mortalidad = float(6.0) #float(input("Tasa de mortalidad: "))
poblacion_inicial = int(32625948) #int(input("Población Inicial: "))


def nacimientos():
    N = tasa_de_natalidad / 1000
    global nacimientos_totales
    nacimientos_totales = N * poblacion_inicial
    print(f"Nacimientos: {round(nacimientos_totales)} personas")


nacimientos()


def muertes():
    M = tasa_de_mortalidad / 1000
    global muertes_totales
    muertes_totales = M * poblacion_inicial
    print(f"Muertes: {round(muertes_totales)} personas")


muertes()


def total():
    global total_de_personas_nuevas
    total_de_personas_nuevas = nacimientos_totales - muertes_totales
    print(f"P'(1) = {round(total_de_personas_nuevas)}")


total()


def constante_k():
    global k
    k = total_de_personas_nuevas / poblacion_inicial
    print(f"k = {k}")

constante_k()


def poblacion_final():
    e = math.exp(k)
    pf = poblacion_inicial * e
    print(f"Población Final: {round(pf)} personas")


poblacion_final()