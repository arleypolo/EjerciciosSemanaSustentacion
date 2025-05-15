students = {}

def addStudentsAndCalifications(students):
    nameStudent = input("Ingresa el nombre del estudiante que deseas agregar : ")
    while nameStudent in students :
        print("Este estudiante ya existe, ingresa uno nuevo ")
        nameStudent = input("Ingresa el nombre del estudiante que deseas agregar : ")
    else: 
        while nameStudent.isspace() or len(nameStudent) == 0 :
            print("\033[31m" + "El campo no puede estar vacio, intenta nuevamente : \033[0m")
            nameStudent = input("Ingresa el nombre del estudiante que deseas agregar : ")
        else :
            calification1 = input("Ingresa la primera calificación del estudiante : ")
            calification2 = input("Ingresa la segunda calificación del estudiante : ")
            calification3 = input("Ingresa la tercera calificación del estudiante : ")
            while True :
                try:
                    if float(calification1 and calification2 and calification3) > 0:
                        students[nameStudent] = (calification1,calification2,calification3)
                        print("\033[32m" + f"Estudiante {nameStudent} agregado con exito !  \033[0m")
                        main()
                        break
                    else:
                        print("\033[31m" + "Valor incorrecto, intenta nuevamente : \033[0m")
                        calification1 = input("Ingresa la primera calificación del estudiante : ")
                        calification2 = input("Ingresa la segunda calificación del estudiante : ")
                        calification3 = input("Ingresa la tercera calificación del estudiante : ")
                except :
                    print("\033[31m" + "Valor invalido en alguna de las calificaciones, intente nuevamente\033[0m")
                    calification1 = input("Ingresa la primera calificación del estudiante : ")
                    calification2 = input("Ingresa la segunda calificación del estudiante : ")
                    calification3 = input("Ingresa la tercera calificación del estudiante : ")



def averageStudents(students):
    nameStudent = input("Ingrese el nombre del Estudiante del cual desea saber su promedio : ")
    if nameStudent in students:
        (calification1, calification2, calification3) = students[nameStudent]
        average = (float(calification1) + float(calification2) + float(calification3)) / 3
        print("\033[32m" +f"\nEl promedio del estudiante {nameStudent} es : {average}\033[0m")
        main()
    else:
        print("\033[31m"f"El estudiante {nameStudent} no existe\033[0m")
        averageStudents(students)


def main() :
    print("********************************************************")
    print("                    OPTIONS MENU                 ")
    print("********************************************************")
    print("\n\033[1;92m" + "\n 1 - Add Student \033[0m")
    print("\n\033[1;93m" + "\n 2 - Search average Student \033[0m") 
    print("\n\033[1;91m" + "\n 3 - Exit\033[0m")

    option = input("\nEnter an option : ")

    if option == "1":
        addStudentsAndCalifications(students)
    elif option == "2" :
        averageStudents(students)
    elif option == "3" :
        print("Thank you for using the Student Grade Manager system!")
        quit()
    else:
        print("Enter a valid option")
        main()

main()
