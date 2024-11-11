from socket import *
serverPort = 1337
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
message, clientAddress = serverSocket.recvfrom(2048)
sentence = message.decode()
print(f'Input: {sentence}')
reversedSentence = ' '.join(sentence.split()[::-1])
print(f'Output: {reversedSentence}')
serverSocket.sendto(reversedSentence.encode(), clientAddress)