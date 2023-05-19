import requests
import json

url = 'http://127.0.0.1:8000/api/consultorios/'

def mostrar(id):
    if id == 0:
        peticion = requests.get(url)
        consult = json.loads(peticion.content)
        if len(consult) > 0:
            data = consult['message']
            print(data+"\n")
            print("{:<5} {:<10} {:<15}".format("#","numero","nombre"))
            if data == "Consultorios Listados":
                data = consult['Consultorios']
                num = 0
                for me in data:
                    num = num + 1
                    print("{:<5} {:<10} {:<15} ".format(str(num),me['numero'],me['nombre']))
        print("")
    else:
        peticion = requests.get(url+str(id))
        consult = json.loads(peticion.content)
        print("")
        if len(consult) > 0:
            data = consult["message"]
            print(data+"\n")
            print("{:<8} {:<25} {:<15}".format("numero","nombre","estado"))
            if data == "Consultorio Listado":
                data = consult['Consultorio']
                if data["estado"] == 1:
                    estado = "activo"
                    print("{:<8} {:<25} {:<15}".format(data["numero"],data["nombre"],estado))
                else:
                    estado = "inactivo"
                    print("{:<8} {:<25} {:<15}".format(data["numero"],data["nombre"],estado))
        print("")

def guardar(numero,nombre):
    parametros={"numero":numero,"nombre":nombre}
    peticion = requests.post(url, data = json.dumps(parametros))
    response = json.loads(peticion.content)
    print('Consultorio Guardado!!')

def actualizar(numero, head, body):
    parametros={head:body}
    peticion = requests.patch(url+str(numero), json = parametros)
    print('Consultorio Actualizado!!')

def eliminar(numero):
    peticion = requests.delete(url+str(numero))
    response = json.loads(peticion.content)
    print('Consultorio Eliminado!!')