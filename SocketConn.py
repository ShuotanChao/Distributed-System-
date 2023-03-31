# echo-client.py
import socket
import time
import threading


def sending_heartbeat(socket):
    while (1):
        socket.sendall(b"server3")
        time.sleep(10)
        data = socket.recv(1024)
    print(f"Heartbeat: {data!r}")


# # Need to send a message into another place in the socket.
# # or if this message has a tag, it saves another file.
# def sending_message(socket):
#     socket.sendall(b"{THIS IS a Json")
#     time.sleep(10)
#     data = socket.recv(1024)
#     print(f"Received {data!r}")

def printing():
    print('Hello!')
    time.sleep(10)
    print('Hello!')
    time.sleep(10)


def connections():

    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 12345  # The port used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        t1 = threading.Thread(target=sending_heartbeat, args=(s,))

      #  t2 = threading.Thread(target=sending_message, args=(s,))

        t2 = threading.Thread(target=printing)
        t1.start()
        # starting thread 2
        t2.start()

        # wait until thread 1 is completely executed
        t1.join()
        # wait until thread 2 is completely executed
        t2.join()

        # both threads completely executed
        print("Done! All of the Thread processes are completed.")


# # Concurrency : use Asynchronous I/O
# # select() allows you to check for I/O completion on more than one socket.
# # you have to use the GIL (Global Interpreter Lock)
# #
