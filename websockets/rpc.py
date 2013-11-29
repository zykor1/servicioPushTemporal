import sys, math
from autobahn.websocket import connectWS
from twisted.python import log
from twisted.internet import defer, reactor
 
from autobahn.websocket import listenWS
from autobahn.wamp import exportRpc, \
                          WampServerFactory, \
                          WampServerProtocol, WampClientFactory, WampClientProtocol, Handler
 

import urllib2
import urllib
import json
#import threading
from threading import Thread
import time




class notifications():
	@exportRpc
	def changeUserStateConexion(self, event):
		try:
			url = "http://localhost:8000/changeUserStateConexion"
			values = event
			encode = urllib.urlencode(values)
			auxUrl = url + '?' + encode
			req = urllib2.Request(auxUrl)
			response = urllib2.urlopen(req)
			response1 = response.read()
			return json.loads(response1)
		except KeyError:
			return {"error" : "Key don't exist in Json"}





class WampServerFilper(WampServerProtocol):
 
   def onSessionOpen(self):
      self.notifications = notifications()
      self.registerForRpc(self.notifications, "http://filper.com/rpc/notifications#")
      self.registerForPubSub("http://filper.com/pubSub/notifications#", True)

 
if __name__ == '__main__':
 
	if len(sys.argv) > 1 and sys.argv[1] == 'debug':
		log.startLogging(sys.stdout)
		debug = True
	else:
		debug = False
 
 	factory = WampServerFactory("ws://localhost:9000", debugWamp = debug)
	factory.protocol = WampServerFilper
	listenWS(factory)
	reactor.run()