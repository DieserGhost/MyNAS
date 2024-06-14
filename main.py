import json
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Load configuration from nas_conf.json
with open("nas_conf.json", "r") as config_file:
    config = json.load(config_file)

ftp_users = config['nas_users']
ftp_server_config = config['nas_server']

# Create authorizer and add users
authorizer = DummyAuthorizer()
for user_data in ftp_users:
    username = user_data['username']
    password = user_data['password']
    directory = user_data['directory']
    perm = user_data.get('perm', 'elradfmwMT')  # Default permissions if not specified
    authorizer.add_user(username, password, directory, perm=perm)

handler = FTPHandler
handler.authorizer = authorizer

# Start FTP server
host = ftp_server_config['host']
port = ftp_server_config['port']
server = FTPServer((host, port), handler)
print(f"Starting NAS server with {len(ftp_users)} user(s)")
server.serve_forever()
