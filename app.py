# se importa el módulo de matemáticas para poder usar el número de euler
import math

# Se asignan los valores deseados, las tasas y la población inicial
tasa_de_natalidad = float(17.16)
tasa_de_mortalidad = float(6.0)
poblacion_inicial = int(32625948)


# se calculan los nacimientos
def nacimientos():
    # dividimos la tasa de natalidad entre mil, eso nos da la variable "N"
    N = tasa_de_natalidad / 1000
    global nacimientos_totales
    # multiplicamos N por la población inicial para obtener los nacimientos
    nacimientos_totales = N * poblacion_inicial
    print(f"Nacimientos: {round(nacimientos_totales)} personas")


nacimientos()


# se calculan las muertes
def muertes():
    # dividimos la tasa de mortalidad entre mil, eso nos da la variable "M"
    M = tasa_de_mortalidad / 1000
    global muertes_totales
    # multiplicamos M por la población inicial para obtener las muertes
    muertes_totales = M * poblacion_inicial
    print(f"Muertes: {round(muertes_totales)} personas")


muertes()


# se calcula el cambio en la población
def total():
    global total_de_personas_nuevas
    # se restan los nacimientos con las muertes
    total_de_personas_nuevas = nacimientos_totales - muertes_totales
    print(f"P'(1) = {round(total_de_personas_nuevas)}")


total()


# se calcula la constante k
def constante_k():
    global k
    # dividimos el cambio en la población entre la población inicial
    k = total_de_personas_nuevas / poblacion_inicial
    print(f"k = {k}")

constante_k()


# se calcula la población final dentro de 1 año
def poblacion_final():
    # multiplicamos el número de euler por la constante k, el resultado lo guardamos en la variable e
    e = math.exp(k)
    # multiplicamos la población inicial por la variable e, eso nos da la población final
    pf = poblacion_inicial * e
    print(f"Población Final: {round(pf)} personas")


poblacion_final()