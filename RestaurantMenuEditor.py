dishes = {}

def addDishes(dishes):
    nameDishe = input("Ingresa el nombre del plato a agregar : ")
    while nameDishe in dishes :
        print("Este plato ya exuste, ingresa uno nuevo ")
        nameDishe = input("Ingresa el nombre del plato a agregar : ")
    else: 
        while nameDishe.isspace() or len(nameDishe) == 0 :
            print("\033[31m" + "El campo no puede estar vacio, intenta nuevamente : \033[0m")
            nameDishe = input("Ingresa el nombre del plato a agregar : ")
        else :
            priceDishe = input("Ingresa el precio del Plato : ")
            availability = input("Ingresa la disponibilidad del plato : ")
            while True :
                if priceDishe.isdigit() & availability.isdigit()  and int(priceDishe and availability) > 0:
                        dishes[nameDishe] = (priceDishe,availability)
                        print("\033[32m" +f"\nPlato agregado correctamente\033[0m")
                        main()
                        break
                else:
                    print("\033[31m" + "Valor incorrecto, intenta nuevamente : \033[0m")
                    priceDishe = input("Ingresa el precio del plato : ")  
                    availability = input("Ingresa la disponibilidad del plato : ")


def updateAvailability(dishes) :
    nameDishe = input("Enter the name of the dishe you want to update : ")  
    if nameDishe in dishes :                                                
        (priceDishe,availability) = dishes[nameDishe]                                
        print("\033[1;33m" + "\n---------------------------------------------------\033[0m")
        print(f"Name: {nameDishe} -- Price: {priceDishe} ")                                                        
        print("\033[1;33m" + "---------------------------------------------------\033[0m")
        while True:
            newAvailability = input("Enter the new availability for this dishe : ")                
            if newAvailability.isdigit() and int(newAvailability) > 0:                              
                newAvailability = int(newAvailability)
                break
            else:
                print("Invalid option. try again")                                     
        dishes[nameDishe] = (priceDishe,newAvailability)
        print("\n\033[1;32m"+"availability successfully updated" )                                
    else:
        print("\033[1;31m"  + "The dishe is not in inventory\033[0m")
        main()

def calculate_total_dishes(dishes):
    nameDishe = input("ingresa el nombre del plato del cual quieres ver la disponibilidad : ")
    if nameDishe in dishes:
        (priceDishe,availability) = dishes[nameDishe]
        print(f"La disponibilidad del plato {nameDishe} es  {availability} y el precio es  ${priceDishe}")
    else:
        print("\033[31m" + "El plato no existe \033[0m")
    

def main() :
    print("********************************************************")
    print("                    OPTIONS MENU                 ")
    print("********************************************************")
    print("\n\033[1;92m" + "\n 1 - Add Dishe \033[0m")
    print("\n\033[1;93m" + "\n 2 - update availability \033[0m") 
    print("\n\033[1;91m" + "\n 3 - calculate availability \033[0m")
    print("\n\033[1;91m" + "\n 4 - Exit \033[0m")

    option = input("\nEnter an option : ")

    if option == "1":
        addDishes(dishes)
    elif option == "2" :
        updateAvailability(dishes)
    elif option == "3" :
        calculate_total_dishes(dishes)
    elif option == "4" :
        print("Thank you for using the Student Grade Manager system!")
        quit()
    else:
        print("Enter a valid option")
        main()

main()


