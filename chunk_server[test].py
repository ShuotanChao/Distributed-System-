
# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
# import time
# import unusefile.menutest as menutest
import SocketConn
import UpdateUserList


if __name__ == '__main__':
    # creating thread

    # Sending hearbeats to the server regularly.
    t1 = threading.Thread(target=SocketConn.connections)
    # Here is the workplace of the client
    # t2 = threading.Thread(target=menutest.combine)
    t2 = threading.Thread(target=UpdateUserList.sendingdata)
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done! All of the Thread processes are completed.")
