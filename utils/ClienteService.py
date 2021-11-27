import socket
import pickle

# Função que imprime a lista formatada
def imprime(l):
    texto = ''
    for i in l:
        texto = texto + '{:>8.2f}'.format(i)
    print(texto)

def ClientData():
    # Cria o socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Tenta se conectar ao servidor
        s.connect((socket.gethostname(), 9999))
        msg = 'Coletando dados...'

        # Envia mensagem vazia apenas para indicar a requisição
        s.send(msg.encode('ascii'))
        bytes = s.recv(10240)

        # Converte os bytes para lista
        lista = pickle.loads(bytes)

        msg = 'end'
        s.send(msg.encode('ascii'))
    except Exception as erro:
        print(str(erro))

    # Fecha o socket
    s.close()
    return lista