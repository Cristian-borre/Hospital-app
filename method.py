import requests
import json

url = 'http://127.0.0.1:8000/api/medicos/'

def mostrar(id):
    if id == 0:
        peticion = requests.get(url)
        medicos = json.loads(peticion.content)
        print("")
        print("{:<5} {:<15} {:<15} {:<15} {:<15}".format("#","documento","nombre","apellido","telefono"))
        num = 0
        for me in medicos['Medicos']:
            num = num + 1
            print("{:<5} {:<15} {:<15} {:<15} {:<15}".format(str(num),me['documento'],me['nombre'],me['apellido'],me['telefono']))
        print("")
    else:
        peticion = requests.get(url+str(id))
        medicos = json.loads(peticion.content)
        print("")
        print("{:<15} {:<15} {:<15} {:<15} {:<5}".format("documento","nombre","apellido","telefono","estado"))
        data = medicos['Medico']
        if data["estado"] == 1:
            estado = "activo"
            print("{:<15} {:<15} {:<15} {:<15} {:<5}".format(data["documento"],data["nombre"],data["apellido"],data["telefono"],estado))
        else:
            estado = "inactivo"
            print("{:<15} {:<15} {:<15} {:<15} {:<5}".format(data["documento"],data["nombre"],data["apellido"],data["telefono"],estado))
        print("")

def guardar(documento,nombre,apellido,telefono):
    parametros={"documento":documento,"nombre":nombre,"apellido":apellido,"telefono":telefono}
    peticion = requests.post(url, data = json.dumps(parametros))
    response = json.loads(peticion.content)
    print('Medico Guardado!!')

def editar(id,documento,nombre,apellido,telefono):
    parametros={"documento":documento,"nombre":nombre,"apellido":apellido,"telefono":telefono}
    peticion = requests.put(url+str(id), data = json.dumps(parametros))
    response = json.loads(peticion.content)
    print('Medico Actualizado!!')