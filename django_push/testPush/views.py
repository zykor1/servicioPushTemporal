# Create your views here.


#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from push.views import *
from push.notificationsHelper import *


# Muestra los cupones. El decorador @page_template, sirve para
# paginar estilo twitter los cupones
def indexTest(request):
        return render_to_response('indexTest.html', context_instance=RequestContext(request))



# Este es para registrar una nueva empresa
def enviaNotificacion(request):
    if (request.GET != {}):
        auxDatos = request.GET
        sendNotification(auxDatos["to"], auxDatos["from"], auxDatos["activity"], auxDatos["message"], auxDatos["title"])
    	return HttpResponse(json.dumps({"success": "Se ha guardado tu comentario"}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"error": "No se envio"}), content_type="application/json")


# Este es para registrar una nueva empresa
def leeMensajes(request):
	if (request.GET != {}):
		auxDatos = request.GET
		return HttpResponse(getNotification(auxDatos["to"]), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"error": "Sin resultados"}), content_type="application/json") 