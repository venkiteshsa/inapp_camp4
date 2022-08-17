import socket


def server_program():
    host = socket.gethostname() # get the hostname
    port = 5000 #initiate port no above 1024 till 65535
    #HOST = "127.0.0.1" # Standard loopback interface address(localhost)
    #PORT = 65432 # Port to listen on (non-privilaged ports are > 1023)

    server_socket = socket.socket()

    server_socket.bind((host, port))
    #bind host address and port together
    # The bind() function takes tuples as argument
    # configure how many client the server can listen simultaneously

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection form: " + str(address))

    while True:
        #receive data stream
        #it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            #if data is not recieved break
            break
        print("message from client"  + str(address)+ " : "  + str(data))
        data = input(' Send Reply: ')
        conn.send(data.encode()) # send data to the client
    
    conn.close() # close the connection

if __name__ == "__main__":
    server_program()

#The __main__ function is a python convention

#if our python program is imported, the just be there as an 
#imported code and do not run until the user calls
#the function (default behaviour)
#if we directly running it using the command python [prog.py]
#then start the function server_program() automatically