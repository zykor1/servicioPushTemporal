#encoding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db import DatabaseError, IntegrityError
# RequestContext se agrega para poder utilizar la ruta de los archivos estatic se debe poner en todas las Views
from django.template import RequestContext 
from django.shortcuts import redirect
from models import Notification, StatusUserNotification
from django.core import serializers
import datetime
import urllib2
import urllib
import json


# Esta peticion, cambiara el estado del usuario y lo regresara si tuvo exito o  no, y cual es el status actual del usuario
def changeUserStateConexion(request):
	if (request != {}):
		try:
			auxData = request.GET
			message = "Conectado"
			auxStatus =  auxData["status"] in ["True", "true", 1]
			obj, auxState = StatusUserNotification.objects.get_or_create(user=str(auxData["idFacebook"]), defaults={"user":str(auxData["idFacebook"]), "status":auxData["status"] }  )
			if (auxState == False):				
				if (obj.status != auxStatus):
					obj.status = auxStatus
			if (obj.status == False):
				message = "Desconectado"
			obj.save()
			return HttpResponse(json.dumps({"idFacebook": auxData["idFacebook"], "status": obj.status, "message": message}) , content_type="application/json") 
		except DatabaseError as e:
			return HttpResponse(json.dumps({"error": "database error"}) , content_type="application/json") 
		except IntegrityError as e:
			return HttpResponse(json.dumps({"error": "integridad"}) , content_type="application/json")
		except StatusUserNotification.DoesNotExist:
			return HttpResponse(json.dumps({"error": "false"}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"error": "No he recibido informacion"}), content_type="application/json")