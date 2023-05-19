from modulo_tratamiento import method_tratamiento
from modulo_paciente import method_paciente
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
    print("\n======== Menu Tratamientos ========")
    print("1. Listar Tratamientos")
    print("2. Buscar Tratamiento")
    print("3. Registrar Tratamiento")
    print("4. Actualizar Tratamiento")
    print("5. Eliminar Tratamiento")
    print("6. Salir")
    op = int(input("\nDigite una opcion: "))
    print("")
    if op == 1:
        id = 0
        method_tratamiento.mostrar(id)
        repetir()
    elif op == 2:
        id = input("Digite el numero del tratamiento: ")
        method_tratamiento.mostrar(id)
        repetir()
    elif op == 3:
        numero = input("Digite el numero del tratamiento: ")
        if numero == "":
            print("No puede enviar el campo vacio!!")
        else:
            fecha = input("Digite el fecha de asignacion: ")
            if fecha == "":
                print("No puede enviar el campo vacio!!")
            else:
                id = 0
                method_paciente.mostrar(id)
                paciente = input("Digite el id del paciente: ")
                if paciente == "":
                    print("No puede enviar el campo vacio!!")
                else:
                    id = 0
                    method_medicamento.mostrar(id)
                    medicamento = input("Digite el id del medicamento: ")
                    if medicamento == "":
                        print("No puede enviar el campo vacio!!")
                    else:
                        fecha_inicio = input("Digite el fecha de inicio: ")
                        if fecha_inicio == "":
                            print("No puede enviar el campo vacio!!")
                        else:
                            fecha_fin = input("Digite el numero de fecha a terminar: ")
                            if fecha_fin == "":
                                print("No puede enviar el campo vacio!!")
                            else:
                                observacion = input("Digite la observacion del tratamiento: ")
                                if observacion == "":
                                    print("No puede enviar el campo vacio!!")
                                else:
                                    method_tratamiento.guardar(numero,paciente,fecha,medicamento,fecha_inicio,fecha_fin,observacion)
        repetir()
    elif op == 4:
        id = 0
        method_tratamiento.mostrar(id)
        id = input("Digite el numero de tratamiento que desea actualizar: ")
        head = input("Que dato quiere actualizar: ")
        if head == "numero":
            print("El numero no se puede actualizar")
        else:
            body = input("Digite el nuevo "+head+": ")
            method_tratamiento.actualizar(id,head,body)
        repetir()
    elif op == 5:
        id = input("Digite el numero del tratamiento: ")
        if id == "":
            print("No puede enviar el campo vacio!!")
        else:
            method_tratamiento.eliminar(id)
        repetir()
    elif op == 6:
        op = ""
        clear(op)
        import main
        main.Menu()
    else:
        print("\nDigite una opcion valida!!")
        menu()
