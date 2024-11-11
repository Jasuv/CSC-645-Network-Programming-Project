from socket import *
serverPort = 1337
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(2048).decode()
print(f'Input: {sentence}')
reversedSentence = ' '.join(sentence.split()[::-1])
print(f'Output: {reversedSentence}')
connectionSocket.send(reversedSentence.encode())
connectionSocket.close()