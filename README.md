<h1>prtscanr - Port Scanner</h1>

<h2>Description</h2>
In this script, the user is prompted to enter a remote host to scan, and the script then uses the socket library to get the IP address of the remote host. The script then creates a PrettyTable to store the results of the scan, with columns for the port number, status (open or closed), service, and version. <br />
<br/>
The script uses threading to scan all ports between 1 and 1024 simultaneously. Each thread checks the status of a single port, and if the port is open, the thread uses the python-nmap library to determine the name and version of the service running on that port. If the version cannot be determined, it is marked as "Unknown" in the results table. <br/>
<br/>
After all, ports have been scanned, the script prints the results table to the console and writes it to a file named <remote_host>_port_scan_results.txt, where <remote_host> is the name of the remote host that was scanned. The file also includes the total time it took to complete the scan. <br/>


<h2>Languages and Utilities Used</h2>

- <b>Python</b>
- <b>pyfiglet</b>
- <b>Python-nmap</b>


<h2>Walkthrough:</h2>

<p align="center">
Importing Modules: <br/>
<img src="https://i.imgur.com/WuGn5QL.png" height="80%" width="80%">
<br />
<br />
Adding pyfiglet banner:  <br/>
<img src="https://i.imgur.com/XG3YMFQ.png" height="80%" width="80%">
<br />
<br />
Defining the port scanning function; uses python-nmap and sockets:  <br/>
<img src="https://i.imgur.com/RDInUzH.png" height="80%" width="80%">
<br />
<br />
Asking user to input target IP to scan:  <br/>
<img src="https://i.imgur.com/J2q4auG.png" height="80%" width="80%">
<br />
<br />
Adds banner to show user the scan is in progress:  <br/>
<img src="https://i.imgur.com/VdpJvd2.png" height="80%" width="80%">
<br />
<br />
Checks to see the start time of the scan:  <br/>
<img src="https://i.imgur.com/SwqBXdX.png" height="80%" width="80%">
<br />
<br />
Creates PrettyTable:  <br/>
<img src="https://i.imgur.com/yDGXi3P.png" height="80%" width="80%">
<br />
<br />
Adding threading to decrease scan time:  <br/>
<img src="https://i.imgur.com/iLnuikV.png" height="80%" width="80%">
<br />
<br />
Checks the end time of the scan and calculates the total scan time:  <br/>
<img src="https://i.imgur.com/GOFPSo1.png" height="80%" width="80%">
<br />
<br />
Prints the output of the scan onto the terminal and also creates a file with the results:  <br/>
<img src="https://i.imgur.com/tAKZwjC.png" height="80%" width="80%">
<br />
<br />
Demonstration of port scanner:  <br/>
<img src="https://i.imgur.com/guIqpsB.png" height="80%" width="80%">
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
