"""
File: client/lan.py
Author: Jeremiah Nairn

Description: (fill in later)
"""

#neccessary imports
import socket
import threading
import sys

#class that handles the client
class client:
    #function to check if the client is connected
    connected = False

    #constructor
    def __init__(self, server_host=None, server_port=7621):
        #prompt the user for the server IP
        host = input("\nPlease enter the hosts x.x.x.x IPV4 address or  \"self\" to connect to a server on the same device: ")
        #find the hosts IP and place it here
        self.server_host = server_host or (self.get_local_ip() if host.lower() == "self" else host)
        self.server_port = server_port
        #declares the client socket to communicate using IPV4 and TCP
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #gets the local ip by using a dummy connection to google
    def get_local_ip(self):
        #create a dummy IPV4 socket on UDP
        dummy = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        try:
            #"connect" our dummy socket to the google DNS server
            dummy.connect(("8.8.8.8", 80))
            #get the computers IP from the communication
            ip = dummy.getsockname()[0]
        finally:
            #close the socket
            dummy.close()
        #return the IP
        return ip

    #threaded function for handling data recieved from the server while still being able to send data
    def data_handler(self):
        while self.connected == True:
            #recieve the data recieved from the server
            response = self.client_socket.recv(1024)
            #move the acsi cursor up one line and return to the start of the line
            sys.stdout.write("\033[F")  
            sys.stdout.write("\r")
            #clear the rest of the line
            sys.stdout.write("\033[K") 
            sys.stdout.flush()
            #pring the message recieved
            print(f"[CLIENT] Received: {response.decode()}")
            #reprint the prompt so the user can continue typing
            print("Enter a message or command: ", end="", flush=True)
            


    #main function to start the clientside
    def start(self):
        try:
            #connect to the server
            self.client_socket.connect((self.server_host,self.server_port))
            print(f"[CLIENT] Connected to server at {self.server_host}:{self.server_port}")
            #set the connected variable to true
            self.connected = True
            #start the data handler thread
            threading.Thread(target=self.data_handler, daemon=True).start()
            #quick statement for clients
            print("\nType \"cmds\" for a list of commands.")
            #try to prevent errors
            try:
                #where the magic happens
                while True:
                    #prompt for a message
                    message = input("Enter a message or command: ")
                    #case statments to recognize commands
                    match message.lower():
                        #prints a list of commands
                        case "cmds":
                            print("\ncmds || Show Commands")
                            print("quit || Close the Client\n")
                        #quits the client
                        case "quit":
                            print("[CLIENT] Closing Client")
                            break
                        #basically an else statement for cases
                        case _:
                            #send a message to the server
                            self.client_socket.sendall(message.encode())

            except Exception as e:
                print(f"[CLIENT] Connection failed: {e}")
            #when the code breaks, it shuts down the socket
            finally:
                self.connected = False
                self.client_socket.close()
                print("[CLIENT] Disconnected")
        #if there is a timeout error, retry
        except TimeoutError:
            print(f"[CLIENT] Connection Timed Out")
            client.__init__(self)
            client.start(self)
        #if the address is entered improperly, retry
        except socket.gaierror:
            print(f"[CLIENT] IP entered incorrectly")
            client.__init__(self)
            client.start(self)




    





