#! /usr/bin/python

''' Echo server program. '''

HOST = ''
SERV_PORT = 9300
CONN_MAX = 3
LINE_MAX_LEN = 2048


def tcp_conn(sock, addr):
    ''' Process a connection from tcp client. '''
    print 'Accepted new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(LINE_MAX_LEN)
        if not data or data == 'exit':
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr


def main():
    ''' main function for server. '''
    import socket, threading
    sock = socket.socket(socket.AF_INET)
    sock.bind((HOST, SERV_PORT))
    sock.listen(CONN_MAX)
    print 'Waiting for connection...'
    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=tcp_conn, args=(conn, addr))
        thread.start()


if __name__ == '__main__':
    main()
