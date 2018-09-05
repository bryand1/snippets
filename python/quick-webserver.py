import socket

HOST, PORT = '', 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)

print("Serving HTTP on port %s ..." % PORT)
while True:
    conn, addr = sock.accept()
    request = conn.recv(1024)
    print(request)
    response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    conn.sendall(response.encode())
    conn.close()

