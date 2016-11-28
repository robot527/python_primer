#! /usr/bin/python

''' Echo client program. '''

LINE_MAX_LEN = 2048


def main(host, port):
    ''' main function for client. '''
    import socket
    #sock = socket.socket(socket.AF_INET)
    sock = socket.create_connection((host, port))
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
                      help="server tcp port [default: %default]")
    argc = len(argv)
    if argc < 2:
        parser.print_help()
    else:
        (options, args) = parser.parse_args()
        main(options.server, options.port)
