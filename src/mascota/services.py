import json
import requests
from causes.settings import URL_SERVICES

def servicio_buscar_mascotas():
    url = URL_SERVICES + "/buscar/mascotas"   
    try:
        result = requests.get(url)
        print "try"
        if result.status_code == 200:
            print result.json()
            return result.json()
        else:
            return Error_Handler(result.status_code)
    except Exception as e:
        print "exepcion"
        return e
 
def Error_Handler(status_error):
    if status_error == 400:
        return {"error":"Error en datos enviados"}
    elif status_error == 500:
        return {"error":"Ocurrio un error en el servidor por favor intente mas tarde"}
    else:
        return {"error":("Ocurrio un error ({0})".format(status_error))} 
