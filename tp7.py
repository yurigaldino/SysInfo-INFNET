import netifaces

print("\nIPs, GATEWAY E SUBNET MASK\n")
for i in netifaces.interfaces():
        try:
            # Address
            print("     IP Address: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
            print("     Subnet Mask: ", netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
            print("     Gateway: ", netifaces.gateways()['default'][netifaces.AF_INET][0],"\n")

        except:pass