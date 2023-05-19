from modulo_cita import method_cita
from modulo_medico import method_medico
from modulo_paciente import method_paciente
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
    print("\n======== Menu Citas ========")
    print("1. Listar Citas")
    print("2. Buscar Cita")
    print("3. Registrar Cita")
    print("4. Actualizar Cita")
    print("5. Eliminar Cita")
    print("6. Salir")
    op = int(input("\nDigite una opcion: "))
    print("")
    if op == 1:
        id = 0
        method_cita.mostrar(id)
        repetir()
    elif op == 2:
        id = input("Digite el numero de la cita: ")
        method_cita.mostrar(id)
        repetir()
    elif op == 3:
        numero = input("Digite el numero de la cita: ")
        if numero == "":
            print("No puede enviar el campo vacio!!")
        else:
            fecha = input("Digite la fecha: ")
            if fecha == "":
                print("No puede enviar el campo vacio!!")
            else:
                hora = input("Digite la hora: ")
                if hora == "":
                    print("No puede enviar el campo vacio!!")
                else:
                    id = 0
                    method_paciente.mostrar(id)
                    paciente = input("Digite el id del paciente: ")
                    if paciente == "":
                        print("No puede enviar el campo vacio!!")
                    else:
                        id = 0
                        method_medico.mostrar(id)
                        medico = input("Digite el id del medico: ")
                        if medico == "":
                            print("No puede enviar el campo vacio!!")
                        else:
                            id = 0
                            method_consultorio.mostrar(id)
                            consultorio = input("Digite el id del consultorio: ")
                            if consultorio == "":
                                print("No puede enviar el campo vacio!!")
                            else:
                                observacion = input("Digite una observacion: ")
                                if observacion == "":
                                    print("No puede enviar el campo vacio!!")
                                else:
                                    method_cita.guardar(numero,fecha,hora,paciente,medico,consultorio,observacion)
        repetir()
    elif op == 4:
        id = 0
        method_cita.mostrar(id)
        id = input("Digite el numero de la cita que desea actualizar: ")
        opcion = input("Que dato quiere actualizar: ")
        if opcion == 'estado cita':
            print("1) Atendido")
            print("2) Cancelada")
            op = input("Digite el nuevo "+opcion+": ")
            if op == '1':
                head = "estado_cita"
                body = 2
                method_cita.actualizar(id,head,body)
            else:
                head = "estado_cita"
                body = 3
                method_cita.actualizar(id,head,body)
        else:
            body = input("Digite el nuevo "+head+": ")
            method_cita.actualizar(id,head,body)
        repetir()
    elif op == 5:
        id = input("Digite el numero de la cita: ")
        if id == "":
            print("No puede enviar el campo vacio!!")
        else:
            method_cita.eliminar(id)
        repetir()
    elif op == 6:
        op = ""
        clear(op)
        import main
        main.Menu()
    else:
        print("\nDigite una opcion valida!!")
        menu()
