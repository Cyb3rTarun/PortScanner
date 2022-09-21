#---------------------------------------------------------------------------Start of the Code.------------------------------------------------------------------

import sys
import socket


#function for scanning the ipaddress with the portnumber
def tcp_scan(ip_addr, port):
	"""Makes a tcp connection if the socket.connect_ex receives without erros it will verifies whether the port is opened or not."""

    #creating a socket layer.
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #if it is 0 tells the port is opened.
	result = s.connect_ex((ip_addr, port))

    #for printing out the open port details.
	if result == 0:
		print("[+] The port {}/{} is\033[32m 'Opened'\033[0m.".format(ip_addr, port))
    #if the port is closed.
	else:
		print("[+] The Port on {}/{} is\033[31m 'Closed'\033[0m.".format(ip_addr, port))
    #closing the connection.
	s.close()


#Main function.
def main():
    #socket default timeout is set to 0.05
    socket.setdefaulttimeout(0.05)
    print("-"*80)
    #printing the banner.
    print("-------> WELCOME TO THE PORTSCANNER, SCAN YOUR ASSEST TO FIND OPEN PORTS. <-------")
    print('-'*80)

    #try condition to get the input from the user of ipaddress and the port details to scan.
    try:

        #initializing the ipaddress value.
        ip_addr = input("[*] Network Address: ")
        print('-'*80)
        #asking for set of port scans options.
        print("[*] Address your ports for Scanning. ")
        print("---> 1. Well Known Ports.")
        print("---> 2. Range of Ports. ")
        print("---> 3. Custom Range Port.")
        print('-'*80)
        #for getting the options value.
        port_option = int(input("---> Option: "))
        print('-'*80)
        print()

        #if the user options is 1 it will scan for set of popular ports like http, https, socks,......etc,,
        if (port_option == 1):
            #list of common ports.
            port_list = [1,5,7,18,20,21,22,23,25,29,37,42,43,49,53,69,70,79,80,103,108,109,110,115,118,119,137,139,143,150,156,443,1080]
            print("[*] Started scanning on the Network Address {}.".format(ip_addr))
            print()
            #for loop for each and every port number.
            for i in port_list:
                tcp_scan(ip_addr, i)

        #condition-2 for the range of port scan.
        elif (port_option == 2):
            #port scan to begin.
            start_port = int(input("Start Port: "))
            #port scan to end.
            end_port = int(input("End Port: "))
            print('-'*80)
            print("[*] Started scanning on the Network Address {}.".format(ip_addr))
            print()
            #for loop for scanning in range of ports.
            for i in range(start_port, end_port+1):
                tcp_scan(ip_addr, i)
                
        #condition-3 for scanning the custom range of ports.        
        elif(port_option == 3):
            #initialzing the port list.
            port_list = []
            print("Provide the custom range port numbers with a containing a space.")
            #getting the user integer input with spaces to scan for a variety range of ports.
            port_numbers = list(map(int, input().split()))
            print('-'*80)
            print("[*] Started scanning on the Network Address {}.".format(ip_addr))
            print()
            #for loop to scan according to the user input.
            for i in port_numbers:
                tcp_scan(ip_addr, i)
        
        #if the mention option is not valid or lies within the range.
        else:
            print("Option must be within integer value '3'. ")

        
    #exception handling for the user input errors.
    #if the value is invalid like strings or negative values.
    except ValueError as v:
        print("invalid input")
    #if the value is invalid like strings or negative values.
    except UnboundLocalError as u:
        print("invalid input")
    #if the provided ipaddress is invalid or does not match the 32 bits or invalid domain name raises an error.
    except socket.gaierror:
        print("---> Unable to fetch the ipaddress, Provide a Valid IP Adress.")
    print()
    print('-'*80)

#calling the main function.
main()

#---------------------------------------------------------------------------End of the Code.------------------------------------------------------------------
