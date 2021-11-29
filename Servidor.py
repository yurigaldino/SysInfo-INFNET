# Servidor
import socket
import pickle

from utils.tp5 import dataCallsSched, dataDirLayout, dataPidLayout
from utils.tp6 import tp6Data
from utils.tp7 import tp7Data
from utils.geral import dataGeral
from utils.rede1 import dataRede1
from utils.disco import dataDisco
from utils.memoria import dataMemoria
from utils.CPU import dataCPU

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Obtem o nome da máquina
host = socket.gethostname()
porta = 9999
# Associa a porta
socket_servidor.bind((host, porta))
# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)
# Aceita alguma conexão
(socket_cliente, addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    # Recebe pedido do cliente:
    msg = socket_cliente.recv(10240)
    print(msg)
    if msg.decode('ascii') == 'end':
        break

    # Gera a lista de resposta
    resposta = []

    data_TP6_TP7 = []
    data_Sched = []
    data_Dir = []
    data_Pid = []
    data_Geral = []
    data_Rede1 = []
    data_Disco = []
    data_Memoria = []
    data_CPU = []

    #tabela[0]
    #Carrega dados do TP6 e TP7 para depois apender na resposta do servidor 
    for i in tp6Data():
        data_TP6_TP7.append(i)
    for i in tp7Data():
        data_TP6_TP7.append(i)
    
    #tabela[1]
    #Carrega dados de Sched para depois apender na resposta do servidor 
    for i in dataCallsSched():
        data_Sched.append(i)
    
    #tabela[2]
    #Carrega dados de Diretórios para depois apender na resposta do servidor 
    for i in dataDirLayout():
        data_Dir.append(i)
    
    #tabela[3]
    #Carrega dados de Processos para depois apender na resposta do servidor 
    for i in dataPidLayout():
        data_Pid.append(i)
    
    #tabela[4]
    #Carrega dados Gerais para depois apender na resposta do servidor 
    for i in dataGeral():
        data_Geral.append(i)
    
    #tabela[5]
    #Carrega dados de Rede 1 para depois apender na resposta do servidor 
    for i in dataRede1():
        data_Rede1.append(i)

    #tabela[6]
    #Carrega dados de Disco (capacidade total) para depois apender na resposta do servidor 
    for i in dataDisco():
        data_Disco.append(i)
    
    #tabela[7]
    #Carrega dados de Memória (RAM total) para depois apender na resposta do servidor 
    for i in dataMemoria():
        data_Memoria.append(i)
    
    #tabela[8]
    #Carrega dados de Processador (marca, cores e logical) para depois apender na resposta do servidor 
    for i in dataCPU():
        data_CPU.append(i)
    
    #Apenda dados para a resposta do servidor
    resposta.append(data_TP6_TP7)
    resposta.append(data_Sched)
    resposta.append(data_Dir)
    resposta.append(data_Pid)
    resposta.append(data_Geral)
    resposta.append(data_Rede1)
    resposta.append(data_Disco)
    resposta.append(data_Memoria)
    resposta.append(data_CPU)

    # Prepara a lista para o envio
    bytes_resp = pickle.dumps(resposta)
    # Envia os dados
    socket_cliente.send(bytes_resp)

# Fecha socket do servidor e cliente
# socket_cliente.close()
# socket_servidor.close()
