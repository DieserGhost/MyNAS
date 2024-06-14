from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

username = "user"
password = "12345"
directory = "NAS"

authorizer = DummyAuthorizer()
authorizer.add_user(username, password, directory, perm='elradfmwMT')

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 21), handler)
print(f"Starting FTP server for directory: {directory}")
server.serve_forever()
