import socket
import sys
from datetime import datetime

#Define time format
time_format = "%I:%M %p" # Changes time to a 12 hour format with AM/PM

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python port_scanner.py<ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print(f"Scanning target {target}")
start_time = datetime.now()
print(f"Time started: {start_time.strftime(time_format)}")
print("-" * 50)

# Create a list to store open ports
open_ports = []

try:
    # Scan ports from 1 to 1024 (well-known ports)
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

# Add completioon message
end_time = datetime.now()
print("-" * 50)
print(f"\nScan of {target} completed.")
print(f"Open ports: {', '.join(map(str, open_ports))}" if open_ports else "No open ports found.")
print(f"Time ended: {end_time.strftime(time_format)}")
print(f"Total duration: {end_time - start_time}")
print("-" * 50)