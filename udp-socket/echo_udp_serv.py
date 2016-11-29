#! /usr/bin/python

''' Echo server program. '''



def udp_echo(host, port):
    ''' main function for server. '''
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print 'Waiting for request...'
    while True:
        data, addr = sock.recvfrom(2048)
        if not data:
            continue
        print 'Received packet from %s:%s...' % addr
        sock.sendto('Hello, %s!' % data, addr)
    sock.close()


if __name__ == '__main__':
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print "usage: python %s port" % argv[0]
    else:
        udp_echo('', int(argv[1]))
