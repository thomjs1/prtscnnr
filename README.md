<h1>prtscanr - Port Scanner</h1>

<h2>Description</h2>
A simple port scanner created in Python that scans a target IP address and returns the open port number, service and service version. The scanner utilies threading to vastly improve the speed of the scan. Once the scan is finished the results are output to a file for future reference. 

<br/>I used PrettyTable to format the output into a easy to read table and pyfiglet to create a banner with the name of the port scanner.

Future improvements will be added to the scanner.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 


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
Adding pyfiglet banner:  <br/>
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
Adding in threading:  <br/>
<img src="https://i.imgur.com/iLnuikV.png" height="80%" width="80%">
<br />
<br />
Checks end time of scan and calcuates the differnce between start and end times to output the total time of the scan:  <br/>
<img src="https://i.imgur.com/GOFPSo1.png" height="80%" width="80%">
<br />
<br />
Prints the output of the scan onto the terminal and also creates a file with the results:  <br/>
<img src="https://i.imgur.com/tAKZwjC.png" height="80%" width="80%">
<br />
<br />
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
