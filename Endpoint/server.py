from OpenSSL import SSL
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol
from txrestapi.resource import APIResource


from txrestapi.methods import GET, POST, PUT, ALL
class MyServiceResource(APIResource)
    PUT('^/revoke/server')
    def revokeServerCertificate(self, request)
        return "Hello World"

    PUT('^/revoke/client')
    def revokeClientCertificate(self, request)
        return 'Hello World'

class Echo(Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

def verifyCallback(connection, x509, errnum, errdepth, ok):
    if not ok:
        print 'invalid cert from subject:', x509.get_subject()
        return False
    else:
        print "Certs are fine"
    return True

def setupRestApi ():
    api = MyServiceResource()
    site = Site(api, timeout=None)

    return site

if __name__ == '__main__':
    myContextFactory = ssl.DefaultOpenSSLContextFactory(
        'keys/server.key', 'keys/server.crt'
        )

    ctx = myContextFactory.getContext()

    ctx.set_verify(
        SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT,
        verifyCallback
        )

    # Since we have self-signed certs we have to explicitly
    # tell the server to trust them.
    ctx.load_verify_locations("keys/ca.pem")

    site = setupRestApi()
    reactor.listenSSL(8000, site, myContextFactory)
    reactor.run()



