import os, subprocess, platform, nmap

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

def obter_hostnames(host_validos):
    nm = nmap.PortScanner()
    try:
        nm.scan(host)
        print("     IP", host, "possui o nome", nm[host].hostname())
    except:
        #pass
        print("Erro:", host)

def scan_host(host):
    nm = nmap.PortScanner()
    nm.scan(host)
    print(nm[host].hostname())
    for proto in nm[host].all_protocols():
        print("------------------------------")
        print("Protocolo:", proto.upper(),"\n")
        lport = nm[host][proto].keys()
        for port in lport:
            print("     Porta", port, "Estado", nm[host][proto][port]["state"])
        print("\n------------------------------------------------------------")

ip_string = "192.168.0.42"
ip_lista = ip_string.split(".") 
base_ip = ".".join(ip_lista[0:3]) + "." 
print("------------------------------------------------------------")
print("\nTESTE DE IPs DA SUBREDE:", base_ip + "0")
host_validos = verifica_hosts(base_ip)
print("     HOST VÁLIDOS:", host_validos)

for host in host_validos:
    obter_hostnames(host)
    scan_host(host)