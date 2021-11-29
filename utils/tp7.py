import netifaces

def tp7Data():
    data = []
    data.append("IPs, GATEWAYS E SUBNET MASKS\n")
    for i in netifaces.interfaces():
            try:
                # Address
                data.append("     IP Address: " + netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'] + 
                "     Subnet Mask: " + netifaces.ifaddresses(i)[netifaces.AF_INET][0]['netmask'] +  
                "     Gateway: " + netifaces.gateways()['default'][netifaces.AF_INET][0])

            except:pass
    return data 