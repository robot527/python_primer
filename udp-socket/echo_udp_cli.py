#! /usr/bin/python

''' Echo client program. '''


def udp_cli(host, port):
    ''' main function for client. '''
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            data = raw_input("send> ")
        except EOFError:
            print "If you want to quit, press Q key.\n"
            continue
        if data is '':
            print
        elif data in ['q', 'exit']:
            data = raw_input("Do you really want to exit ([y]/n)?")
            if data is not 'n':
                break
        else:
            sock.sendto(data, (host, port))
            print "receive>", sock.recv(2048)
    print 'You closed client successfully.'


if __name__ == '__main__':
    from optparse import OptionParser
    from sys import argv
    usage = "usage: python %prog [options] args"
    parser = OptionParser(usage)
    parser.add_option("-s", "--server",
                      default="127.0.0.1",
                      help="server ip address [default: %default]")
    parser.add_option("-p", "--port",
                      metavar="N", type="int",
                      default="9300",
                      help="server udp port [default: %default]")
    argc = len(argv)
    if argc < 2:
        parser.print_help()
    else:
        (options, args) = parser.parse_args()
        udp_cli(options.server, options.port)
