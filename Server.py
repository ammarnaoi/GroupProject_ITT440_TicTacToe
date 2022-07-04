import socket
import sys
from threading import Thread

# Defining variables
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
num2Eng = {0: ' ', 1: 'O', 4: 'X'}
# points which index is available
available = [(i, j) for i in range(3) for j in range(3)]
# Event Listener for each box
pointerEL = {(i * 3) + j + 1: (i, j) for i in range(3) for j in range(3)}
player_list = []

# Server Initialization
def start_server():
    host = ""
    port = 8888

    # Create socket
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket has been created")


    # Binding
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print("Bind failed. Error : " + str(e))
        sys.exit()

    # Listening
    ServerSocket.listen(5)
    print("Socket now listening")

    while True:
        connection, address = ServerSocket.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=threaded_client, args=(connection, ip, port)).start()
        except socket.error as e:
            print("Thread did not start." + str(e))
            ServerSocket.close()
