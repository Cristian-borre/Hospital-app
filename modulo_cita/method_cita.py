import requests
import json

url = 'http://127.0.0.1:8000/api/citas/'
url_paciente = 'http://127.0.0.1:8000/api/pacientes/'
url_medico = 'http://127.0.0.1:8000/api/medicos/'
url_consultorio = 'http://127.0.0.1:8000/api/consultorios/'

def mostrar(id):
    if id == 0:
        peticion = requests.get(url)
        peticion_paciente = requests.get(url_paciente)
        peticion_medico = requests.get(url_medico)
        peticion_consultorio = requests.get(url_consultorio)
        cita = json.loads(peticion.content)
        cita_paciente = json.loads(peticion_paciente.content)
        cita_medico = json.loads(peticion_medico.content)
        cita_consultorio = json.loads(peticion_consultorio.content)
        if len(cita) > 0:
            data = cita['message']
            print(data+"\n")
            print("{:<5} {:<15} {:<15} {:<15}{:<20}{:<20}{:<30}{:<15}{:<15}".format("#","numero","fecha", "hora", "paciente", "medico", "consultorio", "estado cita", "observacion"))
            if data == "Citas Listadas":
                data = cita['Citas']
                data_paciente = cita_paciente['Pacientes']
                data_medico = cita_medico['Medicos']
                data_consultorio = cita_consultorio['Consultorios']
                num = 0
                for me in data:
                    for pac in data_paciente:
                        for med in data_medico:
                            for consult in data_consultorio:
                               if me['paciente_id'] == pac['id']:
                                   if me['medico_id'] == med['id']:
                                       if me['consultorio_id'] == consult['id']:
                                            if me['estado_cita'] == 1:
                                               estado = 'pendiente'
                                               paciente = pac['nombre']
                                               medico = med['nombre']
                                               consultorio = consult['nombre']
                                               num = num + 1
                                               print("{:<5} {:<15} {:<15} {:<15}{:<20}{:<20}{:<30}{:<15}{:<15}".format(str(num),me['numero'],me['fecha'],me['hora'],paciente,medico,consultorio,estado,me['observacion']))
                                            elif me['estado_cita'] == 2:
                                               estado = 'atendido'
                                               paciente = pac['nombre']
                                               medico = med['nombre']
                                               consultorio = consult['nombre']
                                               num = num + 1
                                               print("{:<5} {:<15} {:<15} {:<15}{:<20}{:<20}{:<30}{:<15}{:<15}".format(str(num),me['numero'],me['fecha'],me['hora'],paciente,medico,consultorio,estado,me['observacion']))
                                            if me['estado_cita'] == 3:
                                               estado = 'cancelada'
                                               paciente = pac['nombre']
                                               medico = med['nombre']
                                               consultorio = consult['nombre']
                                               num = num + 1
                                               print("{:<5} {:<15} {:<15} {:<15}{:<20}{:<20}{:<30}{:<15}{:<15}".format(str(num),me['numero'],me['fecha'],me['hora'],paciente,medico,consultorio,estado,me['observacion']))
        print("")
    else:
        peticion = requests.get(url+str(id))
        cita = json.loads(peticion.content)
        print("")
        if len(cita) > 0:
            data = cita["message"]
            print(data+"\n")
            print("{:<8} {:<25} {:<15}".format("numero","fecha", "hora", "paciente", "medico", "consultorio", "estado cita", "observacion"))
            if data == "Cita Listada":
                data = cita['Cita']
                if data["estado"] == 1:
                    estado = "activo"
                    print("{:<8} {:<25} {:<15}".format(data["numero"],me['fecha'],me['hora'],me['paciente'],me['medico'],me['consultorio'],me['estado_cita'],me['observacion'],estado))
                else:
                    estado = "inactivo"
                    print("{:<8} {:<25} {:<15}".format(data["numero"],me['fecha'],me['hora'],me['paciente'],me['medico'],me['consultorio'],me['estado_cita'],me['observacion'],estado))
        print("")

def guardar(numero,fecha,hora,paciente,medico,consultorio,observacion):
    parametros={"numero":numero,"fecha":fecha,"hora":hora,"paciente_id":paciente,"medico_id":medico,"consultorio_id":consultorio,"observacion":observacion}
    peticion = requests.post(url, json = parametros)
    response = json.loads(peticion.content)
    print('Cita Guardada!!')

def actualizar(numero, head, body):
    parametros={head:body}
    peticion = requests.patch(url+str(numero), json = parametros)
    print('Cita Actualizada!!')

def eliminar(numero):
    peticion = requests.delete(url+str(numero))
    response = json.loads(peticion.content)
    print('Cita Eliminada!!')