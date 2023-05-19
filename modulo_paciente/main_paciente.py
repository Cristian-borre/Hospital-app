from modulo_paciente import method_paciente
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
    print("\n======== Menu Pacientes ========")
    print("1. Listar Pacientes")
    print("2. Buscar Paciente")
    print("3. Registrar Paciente")
    print("4. Actualizar Paciente")
    print("5. Eliminar Paciente")
    print("6. Salir")
    op = int(input("\nDigite una opcion: "))
    print("")
    if op == 1:
        id = 0
        method_paciente.mostrar(id)
        repetir()
    elif op == 2:
        id = input("Digite el numero documento: ")
        method_paciente.mostrar(id)
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
                    if telefono == "":
                        print("No puede enviar el campo vacio!!")
                    else:
                        fecha_nacimiento = input("Digite la fecha de nacimiento: ")
                        if fecha_nacimiento == "":
                            print("No puede enviar el campo vacio!!")
                        else:
                            sexo = input("Digite el sexo: ")
                            if sexo == "":
                                print("No puede enviar el campo vacio!!")
                            else:
                                method_paciente.guardar(documento,nombre,apellido,telefono,fecha_nacimiento, sexo)
        repetir()
    elif op == 4:
        id = 0
        method_paciente.mostrar(id)
        id = input("Digite el documento del paciente que desea actualizar: ")
        head = input("Que dato quiere actualizar: ")
        if head == "documento":
            print("El documento no se puede actualizar")
        else:
            body = input("Digite el nuevo "+head+": ")
            method_paciente.actualizar(id,head,body)
        repetir()
    elif op == 5:
        id = input("Digite el numero de documento: ")
        if id == "":
            print("No puede enviar el campo vacio!!")
        else:
            method_paciente.eliminar(id)
        repetir()
    elif op == 6:
        op = ""
        clear(op)
        import main
        main.Menu()
    else:
        print("\nDigite una opcion valida!!")
        menu()
