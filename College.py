def Menu():
    print("---Menu---")
    print("1.Registrar estudiantes")
    print("2.Mostrar todos los estudiantes y sus cursos")
    print("3.Buscar estudiante por carnet")
    print("4.Salir")
students = {}
allow = False
allow1 = False
count = 0
try:
    while allow == False:
        Menu()
        opt = int(input("Seleccione la opción que desee: "))
        match opt:
            case 1:
                number = int(input("Cuantos estudiantes desea ingresar: "))
                if number <= 0:
                    print("La cantidad ingresada no es valida")
                else:
                    for i in range(number):
                        carnet = f"S{count}"
                        name = input("Ingrese el nombre del estudiante: ")
                        age = int(input("Ingrese la edad del estudiante: "))
                        carrer = input("Ingrese la carrera del estudiante: ")
                        subjects = int(input("Ingrese cuantos cursos lleva el estudiante: "))

            case 2:
                if allow1 == False:
                    print("Aún no hay ningún dato que mostrar")
                else:
                    print("Ahora si ")
            case 3:
                if allow1 == False:
                    print("Aún no hay ningún dato que buscar")
                else:
                    print("Ahora si ")
            case 4:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Error: No se a ingresado el tipo de dato correcto")