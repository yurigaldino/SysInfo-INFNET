import psutil

#Dados de rede
interfaces = psutil.net_if_addrs()
ipv6 = interfaces["Ethernet"][2].address
physical_address = interfaces["Ethernet"][0].address
ip = interfaces["Ethernet"][1].address

layout_rede1 = []

def dataRede1():
    layout_rede1.append(f'{ip}')
    layout_rede1.append(f'{ipv6}')
    layout_rede1.append(f'{physical_address}')

    return layout_rede1