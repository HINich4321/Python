import socket
import sys
import re

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
                if banner:
                    print(f"[+] Port {port} is open: {banner}")
                else:
                    print(f"[+] Port {port} is open: No banner retrieved")
            except:
                print(f"[+] Port {port} is open: Unable to detect version")
        sock.close()
    except:
        pass

def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

if __name__ == "__main__":
    try:
        target = input("Enter target IP address or hostname: ")
        ip_or_host_test = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        test_result = ip_or_host_test.match(target)
        if not test_result:
            target = socket.gethostbyname(target)
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        scan_ports(target, start_port, end_port)
    except KeyboardInterrupt:
        print("\n Exiting Program")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved")
        sys.exit()
    except socket.error:
        print("\n Server not responding")
        sys.exit()
