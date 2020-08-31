import socket

config = { "host": "127.0.0.1", "port": 9797 }
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind( (config["host"], config["port"]) )
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print( data )
            # Echo Back
            #conn.sendall(data)
