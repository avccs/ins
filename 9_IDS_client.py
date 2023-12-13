import socket
def main():
    server_ip = '127.0.0.1'  
    server_port = 8888       

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    message = "This is a test packet with malware."  

    client_socket.send(message.encode('utf-8'))
    print(f"Sent message to server: {message}")

    client_socket.close()

if __name__ == "__main__":
    main()


"""
OUTPUT:-
    Sent message to server: This is a test packet with malware.
"""