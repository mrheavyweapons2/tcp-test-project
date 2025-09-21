"""
File: client/lan.py
Author: Jeremiah Nairn

Description: (fill in later)
"""

#neccessary imports
import socket

#class that handles the client
class lanClient:
    #constructor
    def __init__(self, server_host=None, server_port=7621):
        #find the hosts IP and place it here
        self.server_host = server_host or input("\nPlease enter the hosts 10.x.x.x IPV4 address: ")
        self.server_port = server_port
        #declares the client socket to communicate using IPV4 and TCP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #main function to start the clientside
    def start(self):
        #connect to the server
        self.client_socket.connect((self.server_host,self.server_port))
        print(f"[LAN CLIENT] Connected to server at {self.server_host}:{self.server_port}")
        #quick statement for clients
        print("\nType \"cmds\" for a list of commands.")
        #try to prevent errors
        try:
            #where the magic happens
            while True:
                #prompt for a message
                message = input("Enter a message or command")
                #case statments to recognize commands
                match message.lower():
                    #prints a list of commands
                    case "cmds":
                        print("\ncmds  || Show Commands")
                        print("quit || Close the client")
                    #quits the client
                    case "quit":
                        break
                    #basically an else statement for cases
                    case _:
                        #send a message to the server
                        self.client_socket.sendall(message.encode())
                        #wait for a response
                        response = self.client_socket.recv(1024)
                        print(f"[LAN CLIENT] Received: {response.decode()}")
        #when the code breaks, it shuts down the socket
        finally:
            self.client_socket.close()
            print("[LAN CLIENT] Disconnected")



    





