
personas =[]

for i in range(3):
    cualidades = []
    nombre = input(f"Ingrese el nombre {i+1}: ")
    #nombre="DAVID"
    cualidades.append(nombre)
    apellido_paterno = input(f"Ingrese el apellido paterno {i+1}: ")
    #apellido_paterno = "PEREZ"
    cualidades.append(apellido_paterno)
    apellido_materno = input(f"Ingrese el apellido materno {i+1}: ")
    apellido_materno = "QUEVEDO"
    cualidades.append(apellido_materno)
    edad = input(f"Ingrese la edad {i+1}: ")
    #edad = 20
    cualidades.append(edad)


    personas.append(cualidades)
    print(personas)

if len(personas) == 3:
    print("Los datos ingresados son:")
    for y in range(len(personas)):

      for x in range(len(cualidades)):

        print(f"Persona {personas[y][x]}:")
       

else:
    print("No se han ingresado los datos de las tres personas requeridas.")
