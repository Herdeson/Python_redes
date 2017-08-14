from twisted.internet import protocol, reactor, endpoints
from twisted.protocols import basic

class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.transport.write(self.factory.gestUser(user) +b"\r\n")
        self.transport.loseConnection()

class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def __init__(self, user):
        self.users = user

    def getUSer(self, user):
        return self.users.get(user, b"No such user")

fingerEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
fingerEndpoint.listen(FingerFactory({b'moshez': b'Happy and well'}))
reactor.run()
