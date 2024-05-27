
valores = []

for i in range(3):
    valor = input(f"Introduce el valor {i + 1}: ")
    valores.append(valor)


if len(valores) == 3:
    print("Los valores introducidos son:")
    for valor in valores:
        print(valor)
else:
    print("No se han introducido suficientes valores.")
