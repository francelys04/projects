import json
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from services import *
          
@dajaxice_register
def dajax_buscar_mascotas(request):
    result = servicio_buscar_mascotas()
    print "entro al ajax"
    return json.dumps(result)

