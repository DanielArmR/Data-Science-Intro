def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) ##Variable y cantidad de decimales
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    conversor("colombianos", 3875)
elif opcion == '2':
    conversor("argentinos", 65)
elif opcion == '3':
    conversor("mexicanos", 24)
else:
    print('Ingrese una opción correcta')

# dolares = input("¿Cuantos dolares tienes? ")
# dolares = float(dolares)
# pesos_mexicanos = valor_dolar * dolares
# pesos_mexicanos = round(pesos_mexicanos, 2)
# pesos_mexicanos = str(pesos_mexicanos)
# print("Tienes $" +pesos_mexicanos + " pesos")