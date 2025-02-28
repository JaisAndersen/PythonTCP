from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
isRunning = True
while isRunning:
    sentence = input("Input lowercase sentence:")
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    if sentence == "quit":
        isRunning = False
        print("Connection Closed")
    else:
        print('From Server: ' + modifiedSentence.decode())
clientSocket.close()