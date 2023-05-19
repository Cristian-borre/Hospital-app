from modulo_consultorio import method_consultorio
import os

def repetir():
    op = input("¿Desea salir? (S/n): ")
    if op == "s" or op == "S":
        op = ""
        clear(op)
        import main
        main.Menu()
    elif op == "n" or op == "N":
        clear(op)
    else:
        print("Digite una opcion valida!!")
        repetir()

def clear(op):
    if op == "n" or op == "N":
        os.system("cls")
        menu()
    elif op == "":
        os.system("cls")

def menu():
    print("\n======== Menu Consultorios ========")
    print("1. Listar Consultorios")
    print("2. Buscar Consultorio")
    print("3. Registrar Consultorio")
    print("4. Actualizar Consultorio")
    print("5. Eliminar Consultorio")
    print("6. Salir")
    op = int(input("\nDigite una opcion: "))
    print("")
    if op == 1:
        id = 0
        method_consultorio.mostrar(id)
        repetir()
    elif op == 2:
        id = input("Digite el numero del consultorio: ")
        method_consultorio.mostrar(id)
        repetir()
    elif op == 3:
        numero = input("Digite el numero del consultorio: ")
        if numero == "":
            print("No puede enviar el campo vacio!!")
        else:
            nombre = input("Digite el nombre: ")
            if nombre == "":
                print("No puede enviar el campo vacio!!")
            else:
                method_consultorio.guardar(numero,nombre)
        repetir()
    elif op == 4:
        id = 0
        method_consultorio.mostrar(id)
        id = input("Digite el numero del consultorio que desea actualizar: ")
        head = input("Que dato quiere actualizar: ")
        body = input("Digite el nuevo "+head+": ")
        method_consultorio.actualizar(id,head,body)
        repetir()
    elif op == 5:
        id = input("Digite el numero del consultorio: ")
        if id == "":
            print("No puede enviar el campo vacio!!")
        else:
            method_consultorio.eliminar(id)
        repetir()
    elif op == 6:
        op = ""
        clear(op)
        import main
        main.Menu()
    else:
        print("\nDigite una opcion valida!!")
        menu()
