# PortScanner 🖥️
## Overview :-
A portScanner tool which helps you to find out the Open Ports that are availabe on the target system. It works on the principle of TCP Connection. By using the socket module we will try to establish a connection to the destination Port Address. And if the connection is successfull tell us that the port is Open for connection.

### Popular Port Numbers :-

- Port 20 (udp) – File Transfer Protocol (FTP) for data transfer.
- Port 22 (tcp) – Secure Shell (SSH) protocol for secure logins, ftp, and port forwarding.
- Port 23 (tcp) – Telnet protocol for unencrypted text commutations
- Port 80 (tcp) – World Wide Web HTTP
- Port 53 (udp) - Domain Name System.


## Requirements :-
In order to run the script, your system must have the following programs installed.
- Python. Download it from <a href="https://www.python.org/downloads/">Here.</a>
- Socket Module.

## Usage :-

- Condition 1
```

[*] Network Address: www.google.com 
---> Option: 1
[*] Started scanning on the Network Address www.google.com.
[+] The Port on www.google.com/1 is 'Closed'.
[+] The Port on www.google.com/5 is 'Closed'.
[+] The Port on www.google.com/7 is 'Closed'.
.
.
.
```
- Condition 2
```
---> Option: 2
Start Port: 80
End Port: 90
```
- Condition 3
```
---> Option: 3
Provide the custom range port numbers with a containing a space.
80 443 50
```
- Outputs whether the port on the particular Network Address is opened or not.

## Disclaimer :warning:
- All the information on this profile are meant for developing Hacker Defense attitude among the users and help preventing the hack attacks. I insists that these information shall not be used for causing any kind of damage directly or indirectly. However you may try these codes on your own computer at your own risk.


## Connect With Me 📌


- <a href="https://twitter.com/S_Tarun_" style="font-size:16px;">Twitter</a> 
- <a href="https://www.linkedin.com/in/tarunvenom/" style="font-size:16px;">LinkedIn</a>
