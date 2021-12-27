'''
FTP 靶机
'''

import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    '''
    '''

    dpath = os.path.abspath('.')
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', dpath, perm="elradfmwMT")
    # authorizer.add_anonymous

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(('0.0.0.0', 21), handler)
    server.serve_forever()

if __name__ == '__main__':
    main()