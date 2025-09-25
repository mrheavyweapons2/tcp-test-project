The simplest way to explain this project is that I wanted to learn how TCP and Socket protocol works.
I also never made a python script past a single file before, mostly because I never dove really far into python scripting,
because I prioritized learning C++ for robotics. Now that I am in university and can finally set that aside for a little bit,
I decided to start this project (after realizing my experience in this field was rather lacking).

Enough about me, heres how the program works.

The program is sectioned into 3 core files at this current moment. They are as follows:
main.py (The main file that is the core of the project (obviously))
client/client.py (The client side of the handshake, sends and recieves the message)
server/server.py (The server side of the handshake, recieves and sends a confirmation message)

Main, when executed, prompts the user for 3 options, which looks like this:

Please select one of the following options.   

        1. Server Host on a Local Area Network
        2. Server Host on a Wide Area Network 
        3. Run a Default Client

 Options (1-3):

 When you select either 1 or 2, it uses dynamic importing to import the server module, option 3 imports the client module. Main doesnt change its ways over this, it just starts whatever module was imported using the same command.

 When a server starts, no further imput is required, it just waits for client inputs.

 When running a client, it asks you to enter the servers IP (either public or private, doesnt matter), and then it connects you to it. At this point, you can send TCP handshakes to the server and test everything yourself.
