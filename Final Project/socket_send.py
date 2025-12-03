import socket

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    HOST = "172.20.10.4"
    PORT = 10000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( (HOST, PORT) )
    
    # TODO: Get user input and send it to the server using your TCP socket
    outgoing = input("Send a message to the server: ")
    s.sendall(outgoing.encode("utf-8"))

    # TODO: Receive a response from the server and close the TCP connection
    incoming = s.recv(256)
    print(incoming)
    s.close()
    pass


if __name__ == '__main__':
    main()
