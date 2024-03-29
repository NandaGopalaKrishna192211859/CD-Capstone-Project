import socket

def main():
    # Server settings
    server_ip = '127.0.0.1'  # IP address of the server
    port = 12345

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, port))

    while True:
        # Get user input
        description = input("Enter the description of the operation (or 'exit' to quit): ")

        if description.lower() == 'exit':
            break

        # Send the description to the server
        client_socket.send(description.encode())

        # Receive the generated Python code from the server
        python_code = client_socket.recv(1024).decode()

        # Display the generated Python code
        print("Generated Python Code:")
        print(python_code)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
