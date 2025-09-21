"""
File: server/lan.py
Author: Jeremiah Nairn

Description: Program module that functions as a basic LAN server host for TCP.
"""

#neccessary imports
import socket

#class that serves as the core piece of the server
class lanServer:
    #constructor
    def __init__(self, host=None, port=7621):
        #uses a helper function to get the hosts local IP
        self.host = host or self.get_local_ip()
        #assigns a hardcoded port that i might make customizable later
        self.port = port
        #declares the server socket to run on IPV4 and TCP.
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #changing options, allowing reusability, and enabling said options
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
    
    #function to start the program (execute in main)
    def start(self):
        #setting the server to listen into the server (and not another server)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"[LAN SERVER] Listening on {self.host}:{self.port}")