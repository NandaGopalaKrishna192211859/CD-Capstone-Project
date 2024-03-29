import socket

# Dictionary containing sample inputs and corresponding Python code
sample_inputs = {
    "add": "result = num1 + num2",
    "subtract": "result = num1 - num2",
    "mul": "result = num1 * num2",
    "div": "result = num1 / num2",
    "bubble sort": """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
result = arr[:]
bubble_sort(result)
""",
    "insertion sort": """
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
result = arr[:]
insertion_sort(result)
""",
    "find maximum": "result = max(arr)",
    "find minimum": "result = min(arr)",
    "calculate sum": "result = sum(arr)",
    "increment": """
num = 0
while num < 10:
    num += 1
result = num
""",
    "fibonacci sequence": """
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
result = [fibonacci(i) for i in range(n)]
""",
    "calculate factorial": """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(n)
""",
    "print triangle": """
for i in range(1, n + 1):
    print("*" * i)
""",
    "print diamond": """
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
""",
    "check greater than": """
if num1 > num2:
    result = f"{num1} is greater than {num2}"
elif num1 < num2:
    result = f"{num1} is less than {num2}"
else:
    result = f"{num1} is equal to {num2}"
""",
    "check even or odd": """
if num % 2 == 0:
    result = f"{num} is even"
else:
    result = f"{num} is odd"
""",
    "check positive or negative": """
if num > 0:
    result = f"{num} is positive"
elif num < 0:
    result = f"{num} is negative"
else:
    result = f"{num} is zero"
""",
    "check prime or not": """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
result = is_prime(num)
"""
    # Add more operations and their corresponding Python code here
}

def generate_python_code(operation):
    if operation in sample_inputs:
        return sample_inputs[operation]
    else:
        return "Operation not supported. Please try a different description."

def main():
    # Server settings
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 12345

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(1)
    print("Server listening on port", port)

    while True:  # Run indefinitely
        # Accept a connection
        client_socket, addr = server_socket.accept()
        print("Connection from", addr)

        while True:  # Handle multiple requests from the same client
            # Receive data from the client
            data = client_socket.recv(1024).decode()

            if not data:
                break  # Break the inner loop if no data received

            # Generate Python code
            python_code = generate_python_code(data)

            # Send the generated Python code back to the client
            client_socket.send(python_code.encode())

        # Close the connection
        client_socket.close()

    # Close the server socket (This part will only be reached if the server is terminated)
    server_socket.close()

if __name__ == "__main__":
    main()
