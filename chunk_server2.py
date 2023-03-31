# echo-client.py
import socket
import time
# import sys
# import socket
# import selectors
# import types


# sel = selectors.DefaultSelector()
# messages = [b"Message 1 from client.", b"Message 2 from client."]


# # Initialize of the connection
# def start_connections(host, port, num_conns):
#     server_addr = (host, port)
#     for i in range(0, num_conns):
#         connid = i + 1
#         print(f"Starting connection {connid} to {server_addr}")
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.setblocking(False)
#         # returns an error indicator,
#         # connection is completed, the socket is ready for reading and writing.
#         sock.connect_ex(server_addr)
#         events = selectors.EVENT_READ | selectors.EVENT_WRITE

#         # data send to the server are copied using messages.copy()
#         data = types.SimpleNamespace(
#             connid=connid,
#             msg_total=sum(len(m) for m in messages),
#             recv_total=0,
#             # each connection will call socket.send() and modify the list.
#             # keep track of what the client needs to send. has sent and has received.

#             messages=messages.copy(),
#             outb=b"",
#         )
#         sel.register(sock, events, data=data)


# # server expects the client to close its side of the connection,
# # when it's done sending messages.
# # if client(chunk server) doesn't close, the server will leave the connection open.
# # However, in our case, chunk server keeps open the connection betwee master.
# # Or just sending a heart beat, that I am living. every 10 seconds.

# def service_connection(key, mask):
#     sock = key.fileobj
#     data = key.data
#     if mask & selectors.EVENT_READ:
#         recv_data = sock.recv(1024)  # Should be ready to read
#         if recv_data:
#             data.outb += recv_data
#             print(f"Received {recv_data!r} from connection {data.connid}")
#             data.recv_total += len(recv_data)
#         else:
#             print(f"Closing connection {data.connid}")
#         if not recv_data or data.recv_total == data.msg_total:
#             print(f"Closing connection {data.connid}")
#             sel.unregister(sock)
#             sock.close()
#     if mask & selectors.EVENT_WRITE:
#         if not data.outb and data.messages:
#             data.outb = data.messages.pop(0)
#         if data.outb:
#             print(f"Echoing {data.outb!r} to {data.addr}")
#             print(f"Sending {data.outb!r} to connection {data.connid}")
#             sent = sock.send(data.outb)  # Should be ready to write
#             data.outb = data.outb[sent:]


##  Old version ##
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 12345  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # send() does responsible for returns the number of bytes sent,
    # may be less than the size of the data passed in.
    # you are responsible for checking this and calling many times in while loop.
    # sendall() does not need to using while
    while (1):
        s.sendall(b"server2")
        time.sleep(10)
        data = s.recv(1024)

print(f"Received {data!r}")


# # Concurrency : use Asynchronous I/O
# # select() allows you to check for I/O completion on more than one socket.
# # you have to use the GIL (Global Interpreter Lock)
# #
