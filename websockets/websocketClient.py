import sys
from twisted.python import log
from twisted.internet import reactor
 
from autobahn.websocket import connectWS
from autobahn.wamp import WampClientFactory, WampClientProtocol
import urllib2
import urllib
import json
#import threading
from threading import Thread
import time



class PubSubClient1(WampClientProtocol, Thread):

   def onSessionOpen(self):
      print "Conexion abierta"
      self.subscribeUsuario()
 

   def subscribeUsuario(self):
      aux = "notificacion:inscribe"
      print "aux: %s" % (aux)
      self.prefix("notificacion", "http://example.com/notificacion#")
      self.subscribe(aux, self.onEventInscribe)


   def onEventInscribe(self, topicUri, event):
      print "Conectando usuario"
      self.cambiaEstadoConexion(event)


   def cambiaEstadoConexion(self, event):
      try:
         url = "http://localhost:8000/cambiarEstadoConexion"
         values = event
         encode = urllib.urlencode(values)
         auxUrl = url + '?' + encode
         req = urllib2.Request(auxUrl)
         response = urllib2.urlopen(req)
         response1 = response.read()
         auxTopic = "notificacion:%s" % event["name"]
         self.subscribe(auxTopic, self.onEventNotificacion)
         self.publish(auxTopic, {"userName": "saul", "created": "2013-10-18", "accion" : "notificacion", "mensaje" : response1})
      except KeyError:
         print "El json enviado no tiene los datos requeridos"

   def onEventNotificacion(self, topicUri, event):
      print "recibiendo notificacion"
      print event


   def enviaNotificacion(self, notificacion):
      if (notificacion != {}):
         print "aqui 1"
         notificacion = json.loads(notificacion)
         auxTopic = "notificacion:%s" % notificacion["userName"]
         print "aqui 2" + auxTopic
         self.publish(auxTopic, notificacion)
         print "enviado"
      else:
         print "no enviado"



if __name__ == '__main__':
   
      log.startLogging(sys.stdout)
      factory = WampClientFactory("ws://localhost:9000")
      factory.protocol = PubSubClient1
      connectWS(factory)
      reactor.run()
   