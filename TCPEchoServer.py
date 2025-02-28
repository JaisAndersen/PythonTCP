from socket import *
import threading
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready to recieve")
def handleClient(connectionSocket, adress):
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    print(addr)
    threading.Thread(target = handleClient, args = (connectionSocket, addr)).start()

# while True:
#     connectionSocket, addr = serverSocket.accept()
#     print(addr)
#     sentence = connectionSocket.recv(1024).decode()
#     print(sentence)
#     capitalizedSentence = sentence.upper()
#     connectionSocket.send(capitalizedSentence.encode())
#     connectionSocket.close()