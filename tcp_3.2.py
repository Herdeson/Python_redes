# -*- coding: utf-8 -*-
import argparse, socket

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host,port))
    sock.liste(1)
    print('Listening at', sock.getsockname())
    while True:
        sc, sockname = sock.accept()
        print('Processing up to 1024 bytes at a time from', sockname)
        n = 0
        while True:
            data = sc.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            sc.sendall(output) # send it back uppercase
            n += len(data)
            print('\r %d bytes processed so far' % (n, ) end=' ')
            sys.stdout.flush()
        print()
        sc.close()
        print(' Socket closed')

def client(host, port, bytecount):
    pass
