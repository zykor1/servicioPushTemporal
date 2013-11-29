#encoding:utf-8
from django.db import DatabaseError, IntegrityError
from models import Notification, StatusUserNotification
from django.core import serializers
import datetime
import urllib2
import urllib
import json



# Esta peticion se resolvera cuando se desee saber el estado del usuario remotamente
def getStatusUser(to):
	try:
		auxData = StatusUserNotification.objects.get(user=to)
		return auxData.status
	except DatabaseError as e:
		return "DatabaseError" 
	except IntegrityError as e:
		return "IntegrityError"
	except StatusUserNotification.DoesNotExist:
		return "DoesNotExist"


# Este metodo sera invocado mediante 3 parametros
# @to : El nombre del usuario o a quien le llegara la notificacion
# @from : El nombre del usuario o quien envia la notificacion
# @activity : La vista que se abrira en android
# @message : Mensaje que se le enviara, debe ser String
# @title : El titulo del mensaje debe ser string
# el metodo regresara 3  estados  0, 1, 2
# 0 : Error
# 1 : Se guardo la notificacion y fue enviada por mensaje push
# 2 : Se guardo la notificacion pero no fue enviada por mensaje
def sendNotification(to, _from, activity, message, title):
	try:
		url = "http://localhost:3000/notificacion"
		values = {"to": to, "from": _from, "send_date": datetime.datetime.now(), "activity" : activity, "message" : message, "title": title}
		if (newNotification(values)):
			if (getStatusUser(values["to"])):
				data = urllib.urlencode(values)
				auxUrl = url + '?' + data
				req = urllib2.Request(auxUrl)
				response = urllib2.urlopen(auxUrl)
				response1 = response.read()
				return 1
			else:
				return 2
		else:
			return 0
	except KeyError:
		print "Json has not key"


# Este metodo genera una nueva notificacion en la base datos
# Este metodo no debe ser importado desde otras clases
# @values Es un objeto, que tiene todos los valores que necesita la tabla Notificacion
def newNotification(values):
	try:
		print values
		auxNotification = Notification(to=values["to"], _from=values["from"], send_date=values["send_date"], \
		 activity=values["activity"], message=values["message"], title=values["title"])
		auxNotification.save()
		return True
	except DatabaseError as e:
		return False
	except IntegrityError as e:
		return False


"""
 Devuelve las notificaciones del usuario solicitado
  @userName : Nombre de usuario que se desea buscar sus notificaciones
  @order : Si es None, se mostraran todas las notificaciones, si es True se mostraran todas todas las
  	notificaciones que no hayan sido vistas, si es false, se mostraran todas las notificaciones vistas
"""
def getNotification(userName, order=None):
	try:
		if (order == None):
			auxData = Notification.objects.filter(to=userName)
			data = serializers.serialize('json', auxData)
			return data
		elif (order == True):
			auxData = Notification.objects.filter(to=userName, notification_status=True)
			data = serializers.serialize('json', auxData)
			return data
		elif (order == False):
			auxData = Notification.objects.filter(to=userName, notification_status=False)
			data = serializers.serialize('json', auxData)
			return data
		else:
			return "No valid params"		
	except DatabaseError as e:
		return "DatabaseError" 
	except IntegrityError as e:
		return "IntegrityError"
	except StatusUserNotification.DoesNotExist:
		return "DoesNotExist"