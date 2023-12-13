# https://www.cryptool.org/en/cto/openssl or search cryptool openssl
# in cmd of website type  openssl req -x509 -sha256 -nodes -newkey rsa:2048 -keyout localhost.key -out localhost.crt -days 365
# go down click files and download all three files 


import socket
import ssl
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 4423
client_socket.connect((server_ip, server_port))
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
ssl_client_socket = context.wrap_socket(client_socket, server_hostname=server_ip)
try:
    ssl_client_socket.send(b"Hello, server!")
    response = ssl_client_socket.recv(1024)
    print("Server response:", response.decode())
except ssl.SSLError as e:
    print("SSL Error:", e)
finally:
    ssl_client_socket.close()


# """
# OUTPUT:-
# PS C:\Users\students\Desktop\INS__> python .\sslclient.py
# Server response: Hello, client!
# """
