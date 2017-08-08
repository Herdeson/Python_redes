
# -*- coding: utf-8 -*-
#Cliente servidor TCP simples que enviam e recebem 16 octetos
import argparse, socket

def recvall( sock, length ):
    data = b''
    while len(data) < length:
        more = sock.recv(length-len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def recvall_two( sock ):
    data = b''
    while '\r' not in data.decode('ascii') :
        more = sock.recv(8192)
        if not more:
            raise EOFError('was expecting bytes but only received'
                           ' bytes before the socket closed'
                           )
        data += more
    return data


def server(interface, port):
    #arq = open('dados.txt', mode='w')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print('Listening at ',sock.getsockname())
    #lista = []
    #while True:
    for _ in range(0, 50):
        sc, sockname = sock.accept()
        print('We have accepted a connection from:', sockname )
        print('Socket name:', sc.getsockname())
        print('Socket peer:', sc.getpeername())
        #message = recvall(sc, 16)
        message = recvall_two(sc)
        print(' Incoming sixteen-octet message:', repr(message))
        #lista.append(repr(message))
        #sc.sendall(b'Farewell, client')

        #print(' Reply sent, socket closed')
    #arq.writelines(lista)
    #arq.close()
    sc.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    print('Client has been assigned socket name', sock.getsockname())
    sock.sendall(b'HI THERE')
    reply = recvall(sock, 16)
    print('The server said:', repr(reply))
    sock.close()

if __name__ == '__main__':
    choices={'client': client, 'server': server }
    parser = argparse.ArgumentParser(description='Enviar e receber sobre TCP')
    parser.add_argument('role', choices= choices, help='Which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        'host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default = 1060, help='TCP port default(1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
