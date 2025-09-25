"""
File: main.py
Author: Jeremiah Nairn

Description: Foundation for the program. Sets up the host to the decided role, and allows it to
operate as such. 
"""

#neccessary imports
import importlib

###GOALS:
#1. Keep the code as clean as possible (obviously)
#2. WAN and LAN connections should function in main in the closest way possible for modularity
#3. client and server programs can be run similarly in main, also to keep modularity.
#4. in line with rules 2-3, main should function mostly as a setup script

#other functions go here if you have them
def import_role():
    #need this to declare the module as a global
    global module
    #give the user the following options
    print("\nPlease select one of the following options.\n")
    print("\t1. Server Host on a Local Area Network")
    print("\t2. Server Host on a Wide Area Network")
    print("\t3. Run a Default Client")
    #prompt the user
    role = input("\n Options (1-3): ")
    #try-except error handle for the role input
    try:
        role = int(role)
    except ValueError:
        #if a valueError is spotted, retry, then return to main
        print("Failure, please try again.")
        import_role()
        return
    #if check to make sure the int is working
    if (((role >= 1) and (role <=3)) == False):
        print("Failure, please try again.")
        import_role()
        return

    #if statement options
    if role == 1:
        print("Success, Beginning Server Setup on LAN\n")
        mod = importlib.import_module("server.server")
        module = mod.server(True)
    elif role == 2:
        print("Success, Beginning Server Setup on WAN\n")
        mod = importlib.import_module("server.server")
        module = mod.server(False)
        #print a warning since WAN is difficult to replicate
        print("WARNING: WAN SERVERS ARE CURRENTLY UNTESTED, DUE TO THERE BEING NO WAY")
        print("\tFOR ME TO TEST PORT FORWARD AT THIS POINT, YOU HAVE BEEN WARNED\n")
    elif role == 3:
        print("Success, Beginning Client Setup\n")
        mod = importlib.import_module("client.client")
        module = mod.client()
    #return to main
    return

#main function (where foundational code should go)
def main():
    print("Beginning Setup")
    #prompt the user for their role and import the correct module via dynamic importing
    import_role()
    #start the module
    module.start()
    
    

#execute main
if __name__ == '__main__':
    main()