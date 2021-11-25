""" Servidor recebe conexão do cliente e obtém os dados;
- Servidor envia os dados ao cliente e continua esperando por mais requisições
- O processo servidor termina quando o servidor recebe a mensagem 'fim'.
"""

# Servidor
import socket
import psutil
import pickle

from tp6 import tp6Data
from tp7 import tp7Data

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
    msg = socket_cliente.recv(4096)
    print(msg)
    if msg.decode('ascii') == 'fim':
        break

    # Gera a lista de resposta
    resposta = []

    #Carrega dados do TP6 a lista de resposta do servidor
    for i in tp6Data():
        resposta.append(i)
    
    #Carrega dados do TP7 a lista de resposta do servidor
    for i in tp7Data():
        resposta.append(i)

    # Prepara a lista para o envio
    bytes_resp = pickle.dumps(resposta)
    # Envia os dados
    socket_cliente.send(bytes_resp)

# Fecha socket do servidor e cliente
socket_cliente.close()
# socket_servidor.close()
