import socket

import ujson

CONTENT = ""
with open('index.html') as f:
    CONTENT = f.read()


def start(sta):
    ip = sta.ifconfig()[0]
    # Web Server
    ai = socket.getaddrinfo(ip, 80)
    addr = ai[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(20)
    s.settimeout(2)
    while True:
        # Web loop
        try:
            client_stream = s.accept()[0]
            req = client_stream.readline()
            req = req.decode()
            while True:
                h = client_stream.readline()
                print(h)
                if h == b"" or h == b"\r\n" or h == None:
                    break
            client_stream.write("HTTP/1.1 200 OK\n")
            client_stream.write("Content-Type: text/html\n")
            client_stream.write("Connection: close\n")
            client_stream.write("\n")
            # Search for parameters
            params_begin = req.find('?') + 1
            if params_begin > 0:
                params_end = params_begin + req[params_begin:].find(' ')
                params = req[params_begin:params_end]
                # Parameters to dict
                d = {key: value for (key, value) in [x.split('=') for x in params.split('&')]}
                client_stream.write(ujson.dumps({"status": "Sucesso! Movimentando"}))
                client_stream.close()
            else:
                client_stream.write(CONTENT)
                client_stream.close()
        except:
            # Just wait timeout for web
            pass
    s.close()
