import zen_utils

if __name__== '__main__':
    address = zen_utils.parse_command_line('simple single-thread server')
    listener = zen_utils.create_srv(address)
    zen_utils.accept_connections_forever(listener)
