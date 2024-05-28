
  #En este comando "personas =[] sirve para declarar que vamos a hacer un arreglo en este caso llamado "personas"-"
personas =[]
 #Colocamos un for para indicar los ciclos que va a hacer en este caso 3 la variabe i nos ayuda a ir almacenando los datos de la matriz 
for i in range(3):
      #Empezamos a trabajar con matrices (en este caso 3x3)
    cualidades = []
      #Declaramos nuestra primer variable "nombre" de tipo string (cadena de caracter) y con ayuda del input el usurio puede ingresar los datos los cuales se va a en nuestra varaible i 
    nombre = input(f"Ingrese el nombre {i+1}: ")
      #nombre="DAVID"
      #guardamos nuestro registro en el arreglo llamado "cualidades"
    cualidades.append(nombre)
      #Declaramos nuestra segunda variable "apellido_paterno" de tipo string (cadena de caracter)) y con ayuda del input el usurio puede ingresar los datos los cuales se va a en nuestra varaible i 
    apellido_paterno = input(f"Ingrese el apellido paterno {i+1}: ")
      #apellido_paterno = "PEREZ"
      #guardamos nuestro registro en el arreglo llamado "cualidades"
    cualidades.append(apellido_paterno)
      #Declaramos nuestra tercer variable "apellido_materno" de tipo string (cadena de caracter) y con ayuda del input el usurio puede ingresar los datos los cuales se va a en nuestra varaible i 
    apellido_materno = input(f"Ingrese el apellido materno {i+1}: ")
       #apellido_materno = "QUEVEDO"
      #guardamos nuestro registro en el arreglo llamado "cualidades"
    cualidades.append(apellido_materno)
     #Declaramos nuestra cuarta variable "edad" de tipo entero y con ayuda del input el usurio puede ingresar los datos los cuales se va a en nuestra varaible i 
    edad = input(f"Ingrese la edad {i+1}: ")
    #edad = 20
      #guardamos nuestro registro en el arreglo llamado "cualidades"    
    cualidades.append(edad)

    #Agregamos a nuestro primer arreglo "personas" el segundo arreglo llamado "cualidades" con el objetivo de realizar las matrices
    personas.append(cualidades)
    #Mandamos a imprimir en pantalla el arreglo 
    print(personas)
 #Esta parte del codigo nos permite confirmar que se ingresaron datos 3 veces 
if len(personas) == 3:
    #Manda a imprimir en la pantalla los datos 
    print("Los datos ingresados son:")
    # Recorre la lista segun las coordeandas, en este caso del arreglo de personas 
    for y in range(len(personas)):
     #Recorre la lista mediante coordenadas, en este caso en el arreglo de cualidades 
      for x in range(len(cualidades)):
        #Imprime en pantalla el arreglo de personas segu las coordenadas de x, y 
        print(f"Persona {personas[y][x]}:")
       
 #Si no se cumple con el llenado de las tres personas imprimra en la pantalla el siguente texto con ayuda del else
else:
    print("No se han ingresado los datos de las tres personas requeridas.")
