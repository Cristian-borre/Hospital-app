from modulo_medicamento import method_medicamento
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
    print("\n======== Menu Medicamentos ========")
    print("1. Listar Medicamentos")
    print("2. Buscar Medicamento")
    print("3. Registrar Medicamento")
    print("4. Actualizar Medicamento")
    print("5. Eliminar Medicamento")
    print("6. Salir")
    op = int(input("\nDigite una opcion: "))
    print("")
    if op == 1:
        id = 0
        method_medicamento.mostrar(id)
        repetir()
    elif op == 2:
        id = input("Digite el numero del Medicamento: ")
        method_medicamento.mostrar(id)
        repetir()
    elif op == 3:
        numero = input("Digite el numero del Medicamento: ")
        if numero == "":
            print("No puede enviar el campo vacio!!")
        else:
            nombre = input("Digite el nombre: ")
            if nombre == "":
                print("No puede enviar el campo vacio!!")
            else:
                descripcion = input("Digite la descripcion: ")
                if descripcion == "":
                    print("No puede enviar el campo vacio!!")
                else:
                    method_medicamento.guardar(numero,nombre,descripcion)
        repetir()
    elif op == 4:
        id = 0
        method_medicamento.mostrar(id)
        id = input("Digite el numero del medicamento que desea actualizar: ")
        head = input("Que dato quiere actualizar: ")
        body = input("Digite el nuevo "+head+": ")
        method_medicamento.actualizar(id,head,body)
        repetir()
    elif op == 5:
        id = input("Digite el numero del medicamento: ")
        if id == "":
            print("No puede enviar el campo vacio!!")
        else:
            method_medicamento.eliminar(id)
        repetir()
    elif op == 6:
        op = ""
        clear(op)
        import main
        main.Menu()
    else:
        print("\nDigite una opcion valida!!")
        menu()
