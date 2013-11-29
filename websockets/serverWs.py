import sys

from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.websocket import listenWS
from autobahn.wamp import WampServerFactory, \
                          WampServerProtocol, exportRpc


class MyServerProtocol(WampServerProtocol):

   def onSessionOpen(self):
      ## register a URI and all URIs having the string as prefix as PubSub topic
      self.registerForPubSub("http://example.com/notificacion#", True)

      ## register any URI (string) as topic
      #self.registerForPubSub("", True)


if __name__ == '__main__':

   if len(sys.argv) > 1 and sys.argv[1] == 'debug':
      log.startLogging(sys.stdout)
      debug = True
   else:
      debug = False

   factory = WampServerFactory("ws://localhost:9000", debugWamp = True)
   factory.protocol = MyServerProtocol
   factory.setProtocolOptions(allowHixie76 = True)
   listenWS(factory)

   webdir = File(".")
   web = Site(webdir)
   reactor.listenTCP(8080, web)

   reactor.run()