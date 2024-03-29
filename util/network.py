import socket
import platform


def get_ip_address():
    current_os = platform.system()
    if current_os == 'Windows':
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    else:
        import netifaces as ni
        interfaces = ni.interfaces()
        for interface in interfaces:
            if interface.startswith('en') or interface.startswith('eth'):
                try:
                    ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
                    return ip
                except KeyError:
                    pass

