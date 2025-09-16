# imort socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):

    #Establish the connection
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a server socket
    serverSocket.bind(("127.0.0.1", port))

    #Fill in start
    serverSocket.listen()

    #Fill in end

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
        
        print("Got connection from ", addr)

        try:
            #message = connectionSocket.recv(1024)#Fill in start -a client is sending you a message   #Fill in end 
            message = "0 /helloworld.html"
            filename = message.split()[1]
            #filename = "/helloworld.html"

            #opens the client requested file. 
            #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:], "r+")     #fill in start              #fill in end   )

            #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
            #Fill in start 

            #Content-Type is an example on how to send a header as bytes. There are more!
            outputdata = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"

            #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html

            #Fill in end

            content = ""

            for i in f: #for line in file
                content += f.read()

            #message = (outputdata + content).encode('utf-8')
            content = outputdata.encode('utf-8')

            connectionSocket.sendall(content)

            #print(outputdata)

            #Fill in start - append your html file contents #Fill in end 

            #Send the content of the requested file to the client (don't forget the headers you created)!
            #Send everything as one send command, do not send one line/item at a time!

            # Fill in start

            # Fill in end

            # closing the connection socket

        except Exception as e:
            print(f"Error: {e}")

            #    print(e)
            #   Send response message for invalid request due to the file not being found (404)
            #   Remember the format you used in the try: block!
            #   Fill in start

            #   Fill in end


            #   Close client socket
            #   Fill in start

            #   Fill in end

            #   Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
            #   DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
        finally:
            f.close()
            connectionSocket.close()
    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
