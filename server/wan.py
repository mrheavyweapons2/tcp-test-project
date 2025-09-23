"""
File: server/wan.py
Author: Jeremiah Nairn

Description: Program module that functions as a simple WAN server, which can also perform a
TCP handshake. However, to prevent unauthorized entry, it is password protected.
"""

#neccessary imports
import socket
import threading
import urllib.request

#class that serves as the core piece of the server
class wanServer:
    #constructor
    def __init__(self, host=None, port=7621):
        #uses a helper function to get the hosts public IP
        self.host = host or self.get_public_ip()
        #assigns a hardcoded port that i might make customizable later
        self.port = port
        #declares the server socket to run on IPV4 and TCP.
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #changing options, allowing reusability, and enabling said options
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #gets the users public ip from a website that provides our public IP if we make a connection
    def get_public_ip(self):
        try:
            #sends a request to a website which returns our public ip
            with urllib.request.urlopen("https://api.ipify.org") as response:
                #return the IP
                return response.read().decode("utf-8")
        #error checking for an exception
        except Exception as e:
            print(f"[WAN SERVER] Error fetching public IP: {e}")
            return None
    
    #function for handling client operations
    def client_handler(self, connection, address):
        #informs the server of the connection
        print(f"[WAN SERVER] Connection detected from {address}")
        #error handling for unexpected crashes
        try:
            #begins to take data
            with connection:
                while True:
                    #takes data
                    data = connection.recv(1024)
                    #if data errors, break
                    if not data:
                        break
                    #print the data recieved and send it back out
                    print(f"[WAN SERVER] Recieved from {address}: {data.decode()}")
                    connection.sendall(data)
        #checking for an abrupt connection
        except (ConnectionResetError, BrokenPipeError):
            print(f"[WAN SERVER] {address} disconnected unexpectedly.")
        #checking for an exception error
        except Exception as ex:
            print(f"[WAN SERVER] Error with {address}: {ex}")
        #close the connection
        finally:
            connection.close()
            print(f"[WAN SERVER] Closed connection with {address}")


    
    #function to start the program (execute in main)
    def start(self):
        #setting the server to listen into the server (and not another server)
        self.server_socket.bind(("0.0.0.0", self.port))
        self.server_socket.listen()
        print(f"[WAN SERVER] Listening on {self.host}:{self.port}")
        #while true loop for the server to run on
        while True:
            #detecting connections from clients and starting a thread for them
            print(f"[WAN SERVER] Waiting for connection...")
            connection, address = self.server_socket.accept()
            print(f"[WAN SERVER] Connection accepted from {address}")
            client_line = threading.Thread(target=self.client_handler, args=(connection, address))
            client_line.start()
            print(f"[WAN SERVER] Started client thread for {address}")
        