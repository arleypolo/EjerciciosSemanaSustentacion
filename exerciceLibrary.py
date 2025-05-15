books = {}

def addBooks(books):
    titleBook = input("Ingresa el titulo del libro que deseas agregar : ")
    while titleBook in books :
        print("Este libro ya existe, ingresa uno nuevo ")
        titleBook = input("Ingresa el titulo del libro que deseas agregar : ")
    else: 
        while titleBook.isspace() or len(titleBook) == 0 :
            print("\033[31m" + "El campo no puede estar vacio, intenta nuevamente : \033[0m")
            titleBook = input("Ingresa el titulo del libro que deseas agregar : ")
        else :
            nameAuthor = input("Ingresa el nombre del autor del libro : ")
        while nameAuthor.isspace() or len(nameAuthor) == 0:
            print("\033[31m" + "El campo no puede estar vacio, intenta nuevamente : \033[0m")
            nameAuthor = input("Ingresa el nombre del autor del libro : ")
        else :
            pages = input("Ingresa la cantidad de paginas del libro : ")
            while True :
                if pages.isdigit() and int(pages) > 0:
                    books[titleBook] = (nameAuthor,pages)
                    print("\033[32m" + f"Libro {titleBook} agregado con exito a la Biblioteca!  \033[0m")
                    main()
                    break
                else:
                    print("\033[31m" + "Valor incorrecto, intenta nuevamente : \033[0m")
                    pages = input("Ingresa la cantidad de paginas del libro : ")
                


def findBook(books):
    titleBook = input("Ingresa el titulo del libro que deseas buscar : ")
    if titleBook in books:
        (nameAuthor,pages) = books[titleBook] 
        print("----------------------- Información del libro ---------------------------------")
        print("\033[33m" + f"Title Book :\033[0m {titleBook} ")
        print("\033[33m" + f"Name Author Book :\033[0m {nameAuthor}")
        print("\033[33m" + f"Pages Book :\033[0m {pages}")
        main()

def showAllBooks(books) :
    print("--------------------- Libros Disponibles ------------------------------")
    for book in books.keys(): 
        print(f"Title Book : {book}")
        print("---------------------------------------------------------------------------")


def main() :
    print("********************************************************")
    print("                    OPTIONS MENU                 ")
    print("********************************************************")
    print("\n\033[1;92m" + "\n 1 - Add Book \033[0m")
    print("\n\033[1;93m" + "\n 2 - Search Book \033[0m")                                             #Menu options
    print("\n\033[1;32m" + "\n 3 - List Books \033[0m")
    print("\n\033[1;91m" + "\n 4 - Exit\033[0m")

    option = input("\nEnter an option : ")

    if option == "1":
        addBooks(books)
    elif option == "2" :
        findBook(books)
    elif option == "3" :
        showAllBooks(books)
    elif option == "4" :
        print("Thank you for using the library Book system!")
        quit()  
    else:
        print("Enter a valid option")
        main()

main()