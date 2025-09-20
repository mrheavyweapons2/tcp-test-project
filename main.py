"""
File: main.py
Author: Jeremiah Nairn

Description: Foundation for the program. 
"""

###GOALS:
#1. Keep the code as clean as possible (obviously)
#2. WAN and LAN connections should function in main in the closest way possible for modularity
#3. client and server programs can be run similarly in main, also to keep modularity.
#4. in line with rules 2-3, main should function mostly as a setup script


#other functions go here if you have them
def import_role():
    #give the user the following options
    print("\nPlease select one of the following options.\n")
    print("\t1. Server Host on a Local Area Network")
    print("\t2. Server Host on a Wide Area Network")
    print("\t3. Run a Client on a Local Area Network")
    print("\t4. Run a Client on a Wide Area Network")
    #prompt the user
    role = input("\n Options (1-4): ")
    #try-except error handle for the role input
    try:
        role = int(role)
    except ValueError:
        print("Failure, please try again.")
        import_role()
        return
    #if check to make sure the int is working
    if (((role >= 1) and (role <=4)) == False):
        print("Failure, please try again.")
        import_role()

    #if statement options
    if role == 1:
        print("Success, Beginning Server Setup on LAN")
    elif role == 2:
        print("Success, Beginning Server Setup on WAN")
    elif role == 3:
        print("Success, Beginning Client Setup on LAN")
    elif role == 4:
        print("Success, Beginning Client Setup on WAN")
    #return to main
    return



#main function (where foundational code should go)
def main():
    print("Beginning Setup")
    #prompt the user for their role
    #import it via dynamic importing
    import_role()
    

#execute main
if __name__ == '__main__':
    main()