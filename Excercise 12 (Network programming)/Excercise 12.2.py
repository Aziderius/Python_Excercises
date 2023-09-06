import socket
pagina = input("URL: ")

token = pagina.split("/")
count = 0

try:
    hostname = token[2]
except:
    print("please, enter the URL in proper format")
    quit()

portnum = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((hostname, portnum))
except:
    print("wrong URL, please try again")
    quit()

cmd = f'GET {pagina} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    count = count + len(data)
    print(data.decode(),end='')
print("total of number of character recieved:", count)
mysock.close()