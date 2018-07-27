from eventlet.green import socket
from eventlet.green.OpenSSL import SSL

# insecure context, only for example purposes
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

# create underlying green socket and wrap in SSL
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = SSL.Connection(context, sock)

# configure as server
connection.set_accept_state()
connection.bind(('127.0.0.1', 8443))
connection.listen(50)

# accept one client connection then close up shop
client_conn, addr = connection.accept()
print(client_conn.read(100))
client_conn.shutdown()
client_conn.close()
connection.close()

