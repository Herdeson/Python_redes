import argparse, socket, time

aphorisms = {b'Beutiful is better than?': b'Ugly.',
             b'Explicit is better than?': b'Implicit.',
             b'Simple is better than?': b'Complex.'}

def get_answer(aphorism):
    """ Retorna um elemento do dicionario """
    time.sleep(0.3)
    return aphorisms.get(aphorism, b'Error: Unknow aphorism')

def parse_command_line(description):
    parser=argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP ou hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port')
    args=parser.parse_args()
    addres=(args.host, args.p)
    return addres

def create_srv(address):
    """ Constroi e retorna um socket de escuta do servidor"""

    listener =socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('{} escutando'.format(address))
    return listener

def accept_connections_forever(listener):
    """ Responde sempre conexões recebidas em  um soquete de escuta """

    while True:
        sock, address = listener.accept()
        print('Accept connect from {}'.format(address))
        handle_conversation(sock, address)

def handle_conversation(sock, address):
    """ Conversa com com cliente usando sock ate terminar"""
    try:
        while True:
            handle_request(sock)
    except EOFError :
        print('Cliente socket {} has closed'.format(address))
    except Exception as e:
        print('Cliente socket {} error {}'.format(address, e))
    finally:
        sock.close()

def handle_request(sock):
    """ Recebe solicitação do cliente e envia resposta """
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)

def recv_until(sock, suffix):
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError('receive {!r} then socket closed'.format(message))
        message+= data
    return message
