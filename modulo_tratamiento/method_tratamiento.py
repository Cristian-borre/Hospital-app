import requests
import json

url = 'http://127.0.0.1:8000/api/tratamientos/'

def mostrar(id):
    if id == 0:
        peticion = requests.get(url)
        tratamiento = json.loads(peticion.content)
        if len(tratamiento) > 0:
            data = tratamiento['message']
            print(data+"\n")
            print("{:<5} {:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} ".format("#","numero","paciente","fecha asignada","medicamento","fecha_inicio","fecha_fin","observacion"))
            if data == "Tratamientos Listados":
                data = tratamiento['Tratamientos']
                num = 0
                for me in data:
                    num = num + 1
                    print("{:<5} {:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15}".format(str(num),me["numero"],me["paciente_id"],me["fecha_asignada"],me["medicamento_id"],me["fecha_inicio"],me["fecha_fin"],me["observaciones"]))
        print("")
    else:
        peticion = requests.get(url+str(id))
        tratamiento = json.loads(peticion.content)
        print("")
        if len(tratamiento) > 0:
            data = tratamiento["message"]
            print(data+"\n")
            print("{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<30}{:<15}".format("numero","paciente","fecha asignada","medicamento","fecha_inicio","fecha_fin","observacion","estado"))
            if data == "Tratamiento Listado":
                data = tratamiento['Tratamiento']
                if data["estado"] == 1:
                    estado = "activo"
                    print("{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<30}{:<15}".format(data["numero"],data["paciente_id"],data["fecha_asignada"],data["medicamento_id"],data["fecha_inicio"],data["fecha_fin"],data["observaciones"],estado))
                else:
                    estado = "inactivo"
                    print("{:<15} {:<15} {:<20} {:<15} {:<15} {:<15} {:<30}{:<15}".format(data["numero"],data["paciente_id"],data["fecha_asignada"],data["medicamento_id"],data["fecha_inicio"],data["fecha_fin"],data["observaciones"],estado))
        print("")

def guardar(numero,paciente,fecha,medicamento,fecha_inicio,fecha_fin,observacion):
    parametros={"numero":numero,"paciente_id":paciente,"fecha_asignada":fecha,"medicamento_id":medicamento,"fecha_inicio":fecha_inicio,"fecha_fin":fecha_fin,"observaciones":observacion}
    peticion = requests.post(url, json = parametros)
    response = json.loads(peticion.content)
    print('Tratamiento Guardado!!')

def actualizar(numero, head, body):
    parametros={head:body}
    peticion = requests.patch(url+str(numero), json = parametros)
    print('Tratamiento Actualizado!!')

def eliminar(numero):
    peticion = requests.delete(url+str(numero))
    response = json.loads(peticion.content)
    print('Tratamiento Eliminado!!')