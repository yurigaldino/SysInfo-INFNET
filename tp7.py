import netifaces

def tp7Data():
    data = []
    data.append("\nIPs, GATEWAY E SUBNET MASK\n")
    for i in netifaces.interfaces():
            try:
                # Address
                data.append("     IP Address: " + netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
                data.append("     Subnet Mask: " + netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'])
                data.append("     Gateway: " + netifaces.gateways()['default'][netifaces.AF_INET][0] + "\n")

            except:pass
    return data 