import socket
import sys



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created successfully!')
except socket.error as err:
    print('Socket creation failed with error: {}'.format(err))
print(s)
#first parameter stands for IPv4. The second is connection oriented TCP (transmission control protocol) Protocol.
#ip = socket.gethostbyname('www.google.com') <- ip of google.com site
#print(ip)

port = 80

try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror: #gaierror means the problem with DNS(domain name service)
    print('error resolving the host')
    sys.exit()

s.connect((host_ip, port))
print(f'Socket connected successfully to github on port = {host_ip}')


