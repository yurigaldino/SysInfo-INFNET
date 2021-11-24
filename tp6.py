import os, subprocess, platform, nmap, socket

def retorna_codigo_ping(host):
    plataforma = platform.system()
    if (plataforma == "Windows"):
        args = ["ping", "-n", "1", "-l", "1", "-w", "1000", host]
    else:
        args = ["ping", "-c", "1", "-W", "1", host]
    retorno = subprocess.call(args, stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"))
    return retorno

def verifica_hosts(base_ip):
    print("\n     (Verificando)\n", end="")
    host_validos = []
    for i in range(1, 20):
        if ((i % 5) == 0):
            print("\n     .", end="")
        ip = base_ip + str(i)
        retorno = retorna_codigo_ping(ip)
        if (retorno == 0):
            host_validos.append(ip)
    print()
    return host_validos

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    My_ip=s.getsockname()[0]
    s.close()
    print("Meu IP: ",My_ip)
    return My_ip

def tp6Data():
    data = []
    ip_lista = get_ip_address().split(".") 
    base_ip = ".".join(ip_lista[0:3]) + "." 
    data.append("------------------------------------------------------------")
    data.append("\nTESTE DE IPs DA SUBREDE: " + str(base_ip) + "0\n")
    host_validos = verifica_hosts(base_ip)
    data.append("     HOST VÁLIDOS: " + str(host_validos))

    for host in host_validos:

        #obter_hostnames(host)
        nm = nmap.PortScanner()
        try:
            nm.scan(host)
            data.append("     IP " + str(host) + " possui o nome " + str(nm[host].hostname()))
        except:
            #pass
            print("Erro:", host)

        
        #scan_host(host)
        nm = nmap.PortScanner()
        nm.scan(host)
        data.append(nm[host].hostname())
        for proto in nm[host].all_protocols():
            data.append("------------------------------")
            data.append("Protocolo:" + str(proto.upper()) + "\n")
            lport = nm[host][proto].keys()
            for port in lport:
                data.append("     Porta " + str(port) + " Estado " + str(nm[host][proto][port]["state"]))
            data.append("\n------------------------------------------------------------")
    return data