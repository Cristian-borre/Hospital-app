import requests
import json

url = 'http://127.0.0.1:8000/api/medicamentos/'

def mostrar(id):
    if id == 0:
        peticion = requests.get(url)
        consult = json.loads(peticion.content)
        if len(consult) > 0:
            data = consult['message']
            print(data+"\n")
            print("{:<5} {:<10} {:<20} {:<15}".format("#","numero","nombre","descripcion"))
            if data == "Medicamentos Listados":
                data = consult['Medicamentos']
                num = 0
                for me in data:
                    num = num + 1
                    print("{:<5} {:<10} {:<20} {:<15}".format(str(num),me['numero'],me['nombre'],me['descripcion']))
        print("")
    else:
        peticion = requests.get(url+str(id))
        medicamentos = json.loads(peticion.content)
        print("")
        if len(medicamentos) > 0:
            data = medicamentos["message"]
            print(data+"\n")
            print("{:<8} {:<25} {:<15} {:<15}".format("numero","nombre","descripcion","estado"))
            if data == "Tratamiento Listado":
                data = medicamentos['Tratamiento']
                if data["estado"] == 1:
                    estado = "activo"
                    print("{:<8} {:<25} {:<15} {:<15}".format(data["numero"],data["nombre"],data["descripcion"],estado))
                else:
                    estado = "inactivo"
                    print("{:<8} {:<25} {:<15}".format(data["numero"],data["nombre"],data["descripcion"],estado))
        print("")

def guardar(numero,nombre,descripcion):
    parametros={"numero":numero,"nombre":nombre,"descripcion":descripcion}
    peticion = requests.post(url, data = json.dumps(parametros))
    response = json.loads(peticion.content)
    print('Medicamento Guardado!!')

def actualizar(numero, head, body):
    parametros={head:body}
    peticion = requests.patch(url+str(numero), json = parametros)
    print('Medicamento Actualizado!!')

def eliminar(numero):
    peticion = requests.delete(url+str(numero))
    response = json.loads(peticion.content)
    print('Medicamento Eliminado!!')