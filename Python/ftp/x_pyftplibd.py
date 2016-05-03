from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer


def main(username, password, base_dir):
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()
    # Define a new user having full r/w permissions
    authorizer.add_user(username, password, base_dir, perm='elradfmwM')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', 2121)
    server = ThreadedFTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

    # close server
    # server.close_all()


if __name__ == '__main__':
    main('warren', '123456', 'D:\\')
