from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from services import *
from django.template import loader, Context


'''
@summary: 
@param 
'''        
def mascota_list_init(request):
    try:
        context = RequestContext(request)
        return HttpResponse(loader.get_template("mascota/mascota_lista.html").render(context))
    except Exception, e:
        error = e