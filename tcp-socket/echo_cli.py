#! /usr/bin/python

''' Echo client program. '''

HOST = '127.0.0.1'
SERV_PORT = 9300
LINE_MAX_LEN = 2048


def main():
    ''' main function for client. '''
    import socket
    sock = socket.socket(socket.AF_INET)
    sock.connect((HOST, SERV_PORT))
    print sock.recv(LINE_MAX_LEN)
    while True:
        try:
            data = raw_input("send> ")
        except EOFError:
            print "If you want to quit, press Q key.\n"
            continue
        if data is '':
            print
        elif data is 'q':
            data = raw_input("Do you really want to exit ([y]/n)?")
            if data is not 'n':
                sock.send('exit')
                break
        else:
            sock.send(data)
            print "receive>", sock.recv(LINE_MAX_LEN)
    print 'You closed client successfully.'


if __name__ == '__main__':
    main()
