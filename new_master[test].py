import json
import socket
import select

import Heartbeat    # On this file, we will get the function of heartbeat.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set the socket to non-blocking mode
server_socket.setblocking(False)

server_address = ('localhost', 12345)
server_socket.bind(server_address)
server_socket.listen(5)

# List of sockets to be monitored by select
sockets_to_monitor = [server_socket]

print("Server is ready to accept connections...")

# storedata = []

while True:
    # Use select to get the list of sockets ready for reading
    ready_to_read, _, _ = select.select(sockets_to_monitor, [], [])

    for sock in ready_to_read:
        if sock == server_socket:
            # A new client connection is ready to be accepted
            client_socket, client_address = server_socket.accept()
            print(f"Connected to client {client_address}")
            sockets_to_monitor.append(client_socket)
        else:
            # An existing client sent data or closed the connection
            data = sock.recv(1024)
            if data:
                print(f"Received data from client {client_address}: {data}")
                if data.startswith(b'{"'):

                    data = data.decode('utf-8')
                    with open('userlist.json', 'w') as f:
                        json.dump(data, f)
                    data = data.encode('utf-8')
                    sock.sendall(data)
                # If the data is start with nothing. (which means heartbeat data)
                elif data.startswith(b''):
                    # Send the data to the client
                    Heartbeat.update_hearbeat(data.decode())
                    sock.sendall(data)
            else:
                print(f"Connection closed by client {client_address}")
                sock.close()
                sockets_to_monitor.remove(sock)


# Need to solve those issues
# When chunk server accidentally break the connection
# ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
