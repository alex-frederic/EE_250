import socket

def send_image(image_path, host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read(1024)  # Send data in chunks
            while image_data:
                s.send(image_data)
                image_data = image_file.read(1024)

def main():
    # TODO: Create a socket and connect it to the server at the designated IP and port
    HOST = "172.20.10.4"
    PORT = 10000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( (HOST, PORT) )
    
    # # TODO: Get user input and send it to the server using your TCP socket
    # outgoing = input("Send a message to the server: ")
    # s.sendall(outgoing.encode("utf-8"))

    # # TODO: Receive a response from the server and close the TCP connection
    # incoming = s.recv(256)
    # print(incoming)
    # s.close()
    # pass

    with open('rpicamexample.jpg', 'rb') as file:
        print(type(file))
        # data = file.read(1024)  # Read in chunks of 1KB
        # while data:
        #     s.send(data)  # Send image data
        #     data = file.read(1024)


if __name__ == '__main__':
    main()


