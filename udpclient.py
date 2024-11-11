from socket import *
serverName = '127.0.0.1'
serverPort = 1337
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input a sentence: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('From Server:', modifiedMessage.decode())
clientSocket.close()