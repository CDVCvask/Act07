def Menu():
    print("---Menu---")
    print("1.Registrar estudiantes")
    print("2.Mostrar todos los estudiantes y sus cursos")
    print("3.Buscar estudiante por carnet")
    print("4.Salir")
students = {}
allow = False
try:
    while allow == False:
        Menu()
        opt = int(input("Seleccione la opción que desee: "))

except ValueError:
    print("Error: No se a ingresado el tipo de dato correcto")