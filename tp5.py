import PySimpleGUI as pysg
import psutil, os, time, sched, netifaces
from tabulate import tabulate
from hurry.filesize import size, alternative

#Carrega dados no layout_diretorios com o dirFinder()
layout_diretorios = [
    [pysg.Text('Mapeamento de diretórios na raiz do Python:')]
]

#Dados de título de CHAMADA()
dataOut = []

def dirFinder(nome):
    lista = os.listdir()
    dic = {}
    for i in lista:
        if os.path.isfile(i):
            dic[i] = []
            dic[i].append(size(os.stat(i).st_size,system=alternative))
            dic[i].append(os.stat(i).st_atime)
            dic[i].append(os.stat(i).st_mtime)
        else:
            dirName = "(DIR) " + i
            dic[dirName] = []
            dic[dirName].append(size(os.stat(i).st_size,system=alternative))
            dic[dirName].append(os.stat(i).st_atime)
            dic[dirName].append(os.stat(i).st_mtime)

    tabela = [["Nome", "Tamanho", "Data criação", "Data modificação"]]
    for arq in dic:
        linha = [arq]
        linha.append(dic[arq][0])
        linha.append(time.ctime(dic[arq][1]))
        linha.append(time.ctime(dic[arq][2]))
        tabela.append(linha)
        linhaRes = tabulate(tabela, headers='firstrow', tablefmt="tsv")
    # layout_diretorios.append([pysg.Text(f'{linhaRes}', text_color=font_color)])
    dataOut.append("     (CHAMADA) " + str(time.ctime()) + nome)

layout_processos = [
    [pysg.Text("PID    #    Threads   #   Criação    #    T. Usu    #    T. Sis    #    Mem. (%)    #    RSS    #    VMS    #    Executável:")]
]

def mostra_info(pid):
    try:
        p = psutil.Process(pid)
        texto = []
        texto.append(pid)
        texto.append(p.num_threads())
        texto.append(time.ctime(p.create_time()))
        texto.append(round(p.cpu_times().user, 2))
        texto.append(round(p.cpu_times().system, 2))
        texto.append(round(p.memory_percent(), 2))
        rss = round((p.memory_info().rss / (2 ** 20)), 2)
        texto.append(rss)
        vms = round((p.memory_info().vms / (2 ** 20)), 2)
        texto.append(vms)
        exe = p.exe()
        exe = exe.split("\\")
        exe = exe[-1]
        texto.append(exe)
        #print(texto)
        return texto
    except:
        pass

def pidFinder(nome):
    tabela = []
    lista_pids = psutil.pids()
    cont = 0
    for pid in lista_pids:
        texto = mostra_info(pid)
        if (texto != None):
            tabela.append(texto)
            if (cont == 20):
                break
        cont += 1
    linhaRes = tabulate(tabela, headers='firstrow', tablefmt="tsv")    
    # layout_processos.append([pysg.Text(f'{linhaRes}', text_color=font_color)])
    dataOut.append("     (CHAMADA) " + str(time.ctime()) + nome)
# pidFinder()

#Escalonamento de chamadas com sched
scheduler = sched.scheduler(time.time, time.sleep)

def print_event(nome):
    print("EVENTO:", time.ctime(), nome)

def tp5Data():
    data = []
    scheduler.enter(3, 1, dirFinder, ("- INFO: Função de  diretórios",))
    scheduler.enter(6, 1, pidFinder, ("- INFO: Função de  PID's\n",))

    data.append("------------------------------")
    str_title = ("INÍCIO DE ESCALONAMENTO DE CHAMADAS:" + str(time.ctime()) + "\n")
    data.append(str_title)
    print("dataOut")
    print(dataOut)
    for i in dataOut:
        data.append(i)

    t0 = time.perf_counter()
    freq_cpu1 = str(round(psutil.cpu_freq().current, 2))
    scheduler.run()
    sec = round(time.perf_counter() - t0)
    data.append("Tempo de processo do Scheduler antes começar o próximo processo = "+str(sec)+" segundos.") 
    data.append("Ciclos do processador (Frequência ou Clock) utilizados = " + freq_cpu1 + " milhões de hertz por segundo.\n")
    return data
