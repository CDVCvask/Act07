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
subjects = {}
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
                        if age <=10 or age >=120:
                            print("La edad ingresada no es valida")
                        else:
                            carrer = input("Ingrese la carrera del estudiante: ")
                            nsubject = int(input("Ingrese cuantos cursos lleva el estudiante: "))
                            if nsubject <= 0:
                                print("La cantidad ingresada no es valida")
                            else:
                                for j in range(nsubject):
                                    subject_name = input("Ingrese el nombre del curso: ")
                                    homework = int(input("Ingrese la Nota de tarea del estudiante: "))
                                    exam = int(input("Ingrese la nota del examen del estudiante: "))
                                    project = int(input("Ingrese la nota del projecto del estudiante: "))
                                    subjects[subject_name] = {"Tarea": homework, "Examen": exam, "Projecto": project,"number": nsubject}
                                students[carnet] = {"name": name, "age": age, "carrer": carrer, "subject": subjects}
                                count = count + 1
                                allow1 = True
            case 2:
                if allow1 == False:
                    print("Aún no hay ningún dato que mostrar")
                else:
                    cont1 = 1
                    Total = 0
                    print("Todos los estudiantes: ")
                    for code,value in students.items():
                        print(f"Estudiante {cont1}:")
                        print(f"Carnet: {code} Nombre: {value['name']}, Edad: {value['age']}, Carrera: {value['carrer']}")
                        print(f"Cursos del estudiante {cont1}:")
                        for code, grades in value["subject"].items():
                            print(f"{code}: Nota Tareas: {grades['Tarea']}, Nota Examen: {grades['Examen']}, Nota Proyecto: {grades['Projecto']}")
                            avarage = {(grades['Tarea'] + grades['Examen'] + grades['Projecto'])/3}
                            print(f"Promedio del curso = {avarage}")
                            Total = Total + avarage
                        cont1 = cont1 + 1
                        print(f"Promedio total del estudiante = {Total/cont1}")
            case 3:
                if allow1 == False:
                    print("Aún no hay ningún dato que buscar")
                else:
                    look = input("Ingrese el carnet del estudiante que desea encontrar: ")
            case 4:
                print("Gracias por utilizar el programa")
                break
            case _:
                print("La opción seleccionada no es valida")
except ValueError:
    print("Error: No se a ingresado el tipo de dato correcto")