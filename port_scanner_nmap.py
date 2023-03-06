#!/usr/bin/env python


# Importing modules to add various functionality to the script
import socket
import sys
import threading
import time
from datetime import datetime
from prettytable import PrettyTable
import nmap
import pyfiglet


# Adding a fun ascii text banner
ascii_banner = pyfiglet.figlet_format("p r t s c n n r")
print(ascii_banner)


# Define a function for the scanner; this scanner utilizes nmap to pull the name and version of the service on each port
def port_scan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((remoteServerIP, port))
    if result == 0:
        try:
            nm = nmap.PortScanner()
            nm.scan(remoteServerIP, str(port))
            service = nm[remoteServerIP]['tcp'][port]['name']
            version = nm[remoteServerIP]['tcp'][port]['version']
        except:
            service = "Unknown"
            version = "Unknown"
        table.add_row([port, "Open", service, version])
    time.sleep(0.1)


# Asks the user to input the target they would like to scan
remoteServer = input("Target IP: ")
remoteServerIP = socket.gethostbyname(remoteServer)


# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Scanning target IP: ", remoteServerIP)
print("-" * 60)


# Checks what time the scan was started
t1 = datetime.now()


# Creates a table for the results; uses PrettyTable to nicely format the output
table = PrettyTable(["Port", "Status", "Service", "Version"])


# Using threading to scan ports; this greatly speeds up the scan time (here it will scan all ports between 1 and 1024)
threads = []
for port in range(1, 1025):
    thread = threading.Thread(target=port_scan, args=(port,))
    threads.append(thread)
    thread.start()


# Wait for all threads to complete
for thread in threads:
    thread.join()


# Checking the time again now that the scan is finished
t2 = datetime.now()


# Calculates the difference of time, to see how long it took to run the script
total = t2 - t1


# Printing the information to screen
print('Scan finsihed in: ', total)


# Print the results table
print(table)


# Write the results to a file
filename = remoteServer + "_port_scan_results.txt"
with open(filename, "w") as f:
    f.write(str(table))
    f.write("\nScanning Completed in: {}\n".format(total))
print("Results written to", filename)

