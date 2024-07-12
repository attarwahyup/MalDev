import socket
import threading

# Server configuration
SERVER_IP = '127.0.0.1'  # Localhost
SERVER_PORT = 9999  # You can choose any available port

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            if data.lower() == 'exit':
                print("Client disconnected")
                client_socket.close()
                break
            print(f"Received command: {data}")
            
            # Execute the command and send the output back to the client
            if data:
                response = f"Executed: {data}"
                client_socket.send(response.encode())
        except Exception as e:
            print(f"Connection error: {e}")
            client_socket.close()
            break

def start_server():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen(5)
    print(f"[*] Listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        # Wait for a client connection
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a thread to handle the client connection
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
