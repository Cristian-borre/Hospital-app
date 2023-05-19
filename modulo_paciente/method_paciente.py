import requests
import json

url = 'http://127.0.0.1:8000/api/pacientes/'

def mostrar(id):
    if id == 0:
        peticion = requests.get(url)
        paciente = json.loads(peticion.content)
        if len(paciente) > 0:
            data = paciente['message']
            print(data+"\n")
            print("{:<5} {:<15} {:<20} {:<20} {:<15} {:<25} {:<20}".format("#","documento","nombre","apellido","telefono","fecha de nacimiento", "sexo"))
            if data == "Pacientes Listados":
                data = paciente['Pacientes']
                
                num = 0
                for me in data:
                    num = num + 1
                    if me['sexo'] == 1:
                        sexo = "masculino"
                    else:
                        sexo = "femenino"
                    print("{:<5} {:<15} {:<20} {:<20} {:<15} {:<25} {:<20}".format(str(num),me['documento'],me['nombre'],me['apellido'],me['telefono'], me['fecha_nacimiento'], sexo))
        print("")
    else:
        peticion = requests.get(url+str(id))
        paciente = json.loads(peticion.content)
        print("")
        if len(paciente) > 0:
            data = paciente["message"]
            print(data+"\n")
            print("{:<15} {:<20} {:<20} {:<15} {:<20} {:<15} {:<15}".format("documento","nombre","apellido","telefono","fecha nacimiento", "sexo","estado"))
            if data == "Paciente Listado":
                data = paciente['Paciente']
                if data["estado"] == 1:
                    estado = "activo"
                    if data['sexo'] == 1:
                        sexo = "masculino"
                        print("{:<15} {:<20} {:<20} {:<15} {:<20} {:<15} {:<15}".format(data["documento"],data["nombre"],data["apellido"],data["telefono"], data["fecha_nacimiento"], sexo,estado))
                    else:
                        sexo = "femenino"
                        print("{:<15} {:<20} {:<20} {:<15} {:<20} {:<15} {:<15}".format(data["documento"],data["nombre"],data["apellido"],data["telefono"], data["fecha_nacimiento"], sexo,estado))
                else:
                    estado = "inactivo"
                    if data['sexo'] == 1:
                        sexo = "masculino"
                        print("{:<15} {:<20} {:<20} {:<15} {:<20} {:<15} {:<15}".format(data["documento"],data["nombre"],data["apellido"],data["telefono"], data["fecha_nacimiento"], sexo,estado))
                    else:
                        sexo = "femenino"
                        print("{:<15} {:<20} {:<20} {:<15} {:<20} {:<15} {:<15}".format(data["documento"],data["nombre"],data["apellido"],data["telefono"], data["fecha_nacimiento"], sexo,estado))
        print("")

def guardar(documento,nombre,apellido,telefono,fecha_nacimiento,sexo):
    parametros={"documento":documento,"nombre":nombre,"apellido":apellido,"telefono":telefono,"fecha_nacimiento":fecha_nacimiento,"sexo":sexo}
    peticion = requests.post(url, data = json.dumps(parametros))
    response = json.loads(peticion.content)
    print('Paciente Guardado!!')

def actualizar(documento, head, body):
    parametros={head:body}
    peticion = requests.patch(url+str(documento), json = parametros)
    print('Paciente Actualizado!!')

def eliminar(documento):
    peticion = requests.delete(url+str(documento))
    response = json.loads(peticion.content)
    print('Paciente Eliminado!!')