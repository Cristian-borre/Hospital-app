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
        id = input("Digite el id: ")
        method.mostrar(id)
        repetir()
    elif op == 3:
        documento = input("Digite numero de documento: ")
        nombre = input("Digite el nombre: ")
        apellido = input("Digite el apellido: ")
        telefono = input("Digite numero de telefono: ")
        method.guardar(documento,nombre,apellido,telefono)
        repetir()
    elif op == 4:
        id = input("Digite el id: ")
        method.mostrar(id)
        print("1. nombre")
        print("2. apellido")
        print("3. telefono")
        op = int(input("¿Que campo desea editar?: "))
        repetir()
    elif op == 6:
        print("Gracias por usar el programa!!")
        exit
    else:
        print("\nDigite una opcion valida!!")
        Menu()

Menu()