import socket

def is_valid_IP(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        return False