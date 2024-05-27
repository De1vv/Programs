
personas =[]

for i in range(3):
    cualidades = []
    nombre = input(f"Ingrese el nombre {i+1}: ")
    cualidades.append(nombre)
    apellido_paterno = input(f"Ingrese el apellido paterno {i+1}: ")
    cualidades.append(apellido_paterno)
    apellido_materno = input(f"Ingrese el apellido materno {i+1}: ")
    cualidades.append(apellido_materno)

    personas.append(cualidades)
    print(personas)
