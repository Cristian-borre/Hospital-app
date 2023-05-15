import method
import os

def repetir():
    op = input("¿Desea salir? (S/n): ")
    if op == "s" or op == "S":
        exit
    elif op == "n" or op == "N":
        clear(op)
    else:
        print("Digite una opcion valida!!")
        repetir()

def clear(op):
    if op == "n" or op == "N":
        os.system("cls")
        Menu()

def Menu():
    print("\n======== Menu ========")
    print("1. Listar Medicos")
    print("2. Buscar Medico")
    print("3. Registrar Medico")
    print("4. Actualizar Medico")
    print("5. Eliminar Medico")
    print("6. Salir")
    op = int(input("\nDigite una opcion: "))
    print("")
    if op == 1:
        id = 0
        method.mostrar(id)
        repetir()
    elif op == 2:
        id = input("Digite el numero documento: ")
        method.mostrar(id)
        repetir()
    elif op == 3:
        documento = input("Digite el numero de documento: ")
        if documento == "":
            print("No puede enviar el campo vacio!!")
        else:
            nombre = input("Digite el nombre: ")
            if nombre == "":
                print("No puede enviar el campo vacio!!")
            else:
                apellido = input("Digite el apellido: ")
                if apellido == "":
                    print("No puede enviar el campo vacio!!")
                else:
                    telefono = input("Digite el numero de telefono: ")
                    if apellido == "":
                        print("No puede enviar el campo vacio!!")
                    else:
                        method.guardar(documento,nombre,apellido,telefono)
        repetir()
    elif op == 5:
        id = input("Digite el numero de documento: ")
        if id == "":
            print("No puede enviar el campo vacio!!")
        else:
            method.eliminar(id)
        repetir()
    elif op == 6:
        print("Gracias por usar el programa!!")
        exit
    else:
        print("\nDigite una opcion valida!!")
        Menu()

Menu()