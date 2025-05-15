boxes = {}

def addBox(boxes):
    nameBox = input("Ingresa el nombre del tipo de caja a agregar : ")
    while nameBox in boxes :
        print("Este tipo de caja ya existe, ingresa uno nuevo ")
        nameBox = input("Ingresa el nombre del tipo de caja a agregar : ")
    else: 
        while nameBox.isspace() or len(nameBox) == 0 :
            print("\033[31m" + "El campo no puede estar vacio, intenta nuevamente : \033[0m")
            nameBox = input("Ingresa el nombre del tipo de caja a agregar : ")
        else :
            numberBoxes = input("Ingresa la cantidad de cajas : ")
            while True :
                if numberBoxes.isdigit() and int(numberBoxes) > 0:
                        boxes[nameBox] = (numberBoxes)
                        print("\033[32m" +f"\nTipo de caja agregado correctamente\033[0m")
                        main()
                        break
                else:
                    print("\033[31m" + "Valor incorrecto, intenta nuevamente : \033[0m")
                    numberBoxes = input("Ingresa la cantidad de cajas : ")
                    

def updateNumberBox(boxes) :
    nameBox = input("Enter the name of the type Box you want to update : ")  
    if nameBox in boxes :                                              
        (numberBoxes) = boxes[nameBox]                                
        print("\033[1;33m" + "\n---------------------------------------------------\033[0m")
        print(f"Name type Box: {nameBox} -- Numbers: {numberBoxes} ")                                                       
        print("\033[1;33m" + "---------------------------------------------------\033[0m")
        while True:
            newNumberBox = input("Enter the new number Box for this type Box : ")                
            if newNumberBox.isdigit() and int(newNumberBox) > 0:                              
                newNumberBox = int(newNumberBox)
                boxes[nameBox] = (newNumberBox)
                print("\n\033[1;32m"+"Number Box successfully updated" ) 
                main()
                break
            else:
                print("Invalid option. try again")                                     
    else:
        print("\033[1;31m"  + "The type Box is not in inventory\033[0m")


def checkQuantityOfBoxes(boxes) :
    nameTypeBoxes = input(" Ingresa el tipo de cajas del cual quieres verificar la cantidad disponible : ")
    if nameTypeBoxes in boxes:
        (numbersBoxes) = boxes[nameTypeBoxes]
        print("\033[32m" +f"\nLa cantida del Tipo de caja {nameTypeBoxes} es : {numbersBoxes} \033[0m")
    else:
        print("\033[31m" + f"El tipo de caja {nameTypeBoxes} no existe\033[0m")



def main() :
    print("********************************************************")
    print("                    OPTIONS MENU                 ")
    print("********************************************************")
    print("\n\033[1;92m" + "\n 1 - Add Type Box \033[0m")
    print("\n\033[1;93m" + "\n 2 - update Number Box \033[0m") 
    print("\n\033[1;91m" + "\n 3 - Check Quantity of Boxes\033[0m")
    print("\n\033[1;91m" + "\n 4 - Exit \033[0m")

    option = input("\nEnter an option : ")

    if option == "1":
        addBox(boxes)
    elif option == "2" :
        updateNumberBox(boxes)
    elif option == "3" :
        checkQuantityOfBoxes(boxes)
    elif option == "4" :
        print("Thank you for using the Ware House Box Counter Manager system!")
        quit()
    else:
        print("Enter a valid option")
        main()

main()


# 5. Movie Rating System
movies = {}

def add_movie(name):
    movies[name] = []

def rate_movie(name, rating):
    if name in movies:
        movies[name].append(rating)

def average_rating(name):
    if name in movies and len(movies[name]) > 0:
        return sum(movies[name]) / len(movies[name])
    return 0.0


# 6. Online Course Tracker
courses = {}

def add_course(name, duration, enrolled):
    courses[name] = {"duration": duration, "enrolled": enrolled}

def update_enrollment(name, new_enrollment):
    if name in courses:
        courses[name]["enrolled"] = new_enrollment

def filter_by_hour(min_hours):
    result = []
    for name, course in courses.items():
        if course["duration"] >= min_hours:
            result.append(name)
    return result


# 7. To-Do List Organizer
todos = {}

def add_task(name, priority):
    todos[name] = {"priority": priority, "status": "pending"}

def complete_task(name):
    if name in todos:
        todos[name]["status"] = "completed"

def filter_tasks(priority=None, status=None):
    result = []
    for name, task in todos.items():
        if (priority is None or task["priority"] == priority) and \
        (status is None or task["status"] == status):
            result.append(name)
    return result


# 8. Digital Wallet
wallet = {}

def add_expense(category, amount):
    if category in wallet:
        wallet[category] += amount
    else:
        wallet[category] = amount

def total_spent():
    return sum(wallet.values())

def expense_percentages():
    total = total_spent()
    if total == 0:
        return {}
    result = {}
    for category, amount in wallet.items():
        result[category] = (amount / total) * 100
    return result


# 9. Pet Adoption Center
pets = []

def add_pet(name, species, age):
    pets.append({"name": name, "species": species, "age": age})

def find_by_species(species):
    result = []
    for pet in pets:
        if pet["species"] == species:
            result.append(pet)
    return result

def older_than(age):
    result = []
    for pet in pets:
        if pet["age"] > age:
            result.append(pet)
    return result


# 10. Gym Membership System
members = {}

def register_member(name, plan, status):
    members[name] = {"plan": plan, "status": status}

def change_plan(name, new_plan):
    if name in members:
        members[name]["plan"] = new_plan

def unpaid_members():
    result = []
    for name, member in members.items():
        if member["status"] == "late":
            result.append(name)
    return result