import socket
import sys
from threading import Thread

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
num2Eng = {0: ' ', 1: 'O', 4: 'X'}
available = [(i, j) for i in range(3) for j in range(3)]
pointerEL = {(i * 3) + j + 1: (i, j) for i in range(3) for j in range(3)}
player_list = []


def start_server():
    host = ""
    port = 8888

    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket Deployed")

    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print("Bind failed. Error : " + str(e))
        sys.exit()

    ServerSocket.listen(5)
    print("Socket now receiving")

    while True:
        connection, address = ServerSocket.accept()
        ip, port = str(address[0]), str(address[1])
        print("Connected with " + ip + ":" + port)

        try:
            Thread(target=threaded_client, args=(connection, ip, port)).start()
        except socket.error as e:
            print("Thread did not start." + str(e))
            ServerSocket.close()
