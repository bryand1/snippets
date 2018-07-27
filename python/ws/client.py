import socket
import ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8443))
sslSocket = ssl.SSLSocket(s)
# print(repr(sslSocket.server()))
# print(repr(sslSocket.issuer()))
sslSocket.write('Hello secure socket\n'.encode())
s.close()
