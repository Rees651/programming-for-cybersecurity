import socket

host = input("Enter IP Address: ")
port = int(input("Enter Port Number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

result = sock.connect_ex((host, port))

if result == 0:
    print("Port Open")
else:
    print("Port Closed")

sock.close()
