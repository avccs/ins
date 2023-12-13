import socket
import threading

class IDS:
    def __init__(self):
        self.attack_signatures = ['malware', 'exploit', 'attack']
        self.detected_attacks = []

    def detect_attack(self, packet):
        for signature in self.attack_signatures:
            if signature in packet:
                self.detected_attacks.append(signature)
                print(f"Detected {signature} attack in packet: {packet}")

def listen_for_traffic(ids):
    host = '0.0.0.0'
    port = 8888

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:  
        server_socket.bind((host, port))
        server_socket.listen(5)

        print(f"Listening on {host}:{port} for incoming traffic...")

        try:
            while True:
                client_socket, client_addr = server_socket.accept()
                client_ip, client_port = client_addr 

                print(f"Accepted connection from {client_ip}, client_port {client_port}")

                packet = client_socket.recv(1024).decode('utf-8')
                ids.detect_attack(packet)

                accept_count = False
                client_socket.close()

        except KeyboardInterrupt:
            print("Server stopping...")

def main():
    ids = IDS()

    traffic_listener = threading.Thread(target=listen_for_traffic, args=(ids,))
    traffic_listener.start()

if __name__ == "__main__":
    main()


"""
OUTPUT:- 
    Listening on 0.0.0.0:8888 for incoming traffic...
    Accepted connection from 127.0.0.1, client_port 50359
    Detected malware attack in packet: This is a test packet with malware.
"""