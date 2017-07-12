# -*- coding: utf-8 -*-
# Fundamentos de Python Network Programming
# Observando utilização de socket.getaddrinfo
import argparse, socket, sys

def connect_to(hostname_or_ip):
    try:
        infolist =  socket.getaddrinfo(
            hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
            socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME,
        )
    except socket.gaierror as e:
        print('Name service failure: ', e.args[1])
        sys.exit(1)

    info = infolist[0] #Tentar no primeiro servidor da lista
    socket_args = info[0:3]
    address = info[4]
    #print(address)
    s = socket.socket(*socket_args)

    try:
        s.connect(address)
    except socket.error as e:
        print('Network failure: ', e.args[1])
    else:
        print('Success: host {} is listening on port 80'.format(info[3]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tentar conectar a porta 80')
    parser.add_argument('hostname', help='hostname that you want to contact')
    connect_to(parser.parse_args().hostname)
