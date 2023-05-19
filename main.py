from modulo_medico import main_medico
from modulo_consultorio import main_consultorio
from modulo_medicamento import main_medicamento
from modulo_tratamiento import main_tratamiento
from modulo_paciente import main_paciente
from modulo_cita import main_cita
import os

def clear():
    os.system("cls")

def Menu():
    print("\n======== Menu Inicio ========")
    print("1. Medicos")
    print("2. Consultorios")
    print("3. Citas")
    print("4. Pacientes")
    print("5. Tratamientos")
    print("6. Medicamentos")
    print("7. Salir")
    op = int(input("\nDigite una opcion: "))
    print("")
    if op == 1:
        clear()
        main_medico.menu()
    elif op == 2:
        clear()
        main_consultorio.menu()
    elif op == 3:
        clear()
        main_cita.menu()
    elif op == 4:
        clear()
        main_paciente.menu()
    elif op == 5:
        clear()
        main_tratamiento.menu()
    elif op == 6:
        clear()
        main_medicamento.menu()
    elif op == 7:
        print("Gracias por usar el programa!!\n")
        exit()
    else:
        print("\nDigite una opcion valida!!")
        Menu()

Menu()