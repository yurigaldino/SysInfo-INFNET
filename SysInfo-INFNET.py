#Código baseado com internet cabeada (Ethernet) e processador com 12 threads. É necessária adaptação dessas variáveis para funcionamento em outras máquinas e sistemas.

import PySimpleGUI as pysg
from PySimpleGUI.PySimpleGUI import Print
import psutil, platform, cpuinfo, os, time, sched
from tabulate import tabulate
from hurry.filesize import size, alternative

#Setando tema e cor de fonte do sistema
pysg.theme('LightBrown13') #Banco de temas pode ser encontrado aqui: https://user-images.githubusercontent.com/46163555/71361827-2a01b880-2562-11ea-9af8-2c264c02c3e8.jpg
font_color = 'Black'

#Dados de sistema
marca = str(platform.processor())
nome = str(platform.node())
versao = str(platform.platform())
so = str(platform.system())

#Dados de processador
cpu_info = cpuinfo.get_cpu_info()
cores_cpu = psutil.cpu_count(logical=False)
logical_cpu = psutil.cpu_count()

#Dados de memória
mem = psutil.virtual_memory()
mem_total = round(mem.total / pow(2, 30), 2)
porcent_memoria = mem.percent
texto_memoria = str(mem_total) + "GB / " + str(porcent_memoria) + "%"

#Dados de disco
disco = psutil.disk_usage(".")
disco_total = round(disco.total / pow(2, 30), 2)
percent_disco = disco.percent
texto_uso_disco = "(Total: " + str(disco_total) + "GB / " + str(percent_disco) + "%)"

#Dados de rede
interfaces = psutil.net_if_addrs()
ipv6 = interfaces["Ethernet"][2].address
physical_address = interfaces["Ethernet"][0].address
ip = interfaces["Ethernet"][1].address

#Layout de abas
layout_geral = [
    [pysg.Text('SO:')],
    [pysg.Text(f'{so}', text_color=font_color)],
    [pysg.Text('Versão do SO:')],
    [pysg.Text(f'{versao}', text_color=font_color)],
    [pysg.Text('Nome da máquina:')],
    [pysg.Text(f'{nome}', text_color=font_color)],
    [pysg.Text('Arquitetura:')],
    [pysg.Text(f'{cpu_info["arch"]}', text_color=font_color)],
    [pysg.Text('Palavra da CPU:')],
    [pysg.Text(f'{cpu_info["bits"]} bits', text_color=font_color)],
]

layout_cpu = [
    [pysg.Text('Marca do processador:')],
    [pysg.Text(f'{marca}', text_color=font_color)],
    [pysg.Text('Núcleos físicos:')],
    [pysg.Text(f'{cores_cpu} cores', text_color=font_color)],
    [pysg.Text('Núcleos lógicos:')],
    [pysg.Text(f'{logical_cpu} threads', text_color=font_color)],
    [pysg.Text('Frequência total:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-FREQCPU-')],
    [pysg.Text('Uso de CPU (Total):')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-USOCPU-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,20), key='-PROGCPU-')],
]

layout_threads = [
    #[pysg.Text('CPU0:')],
    [pysg.Text('CPU0', text_color=font_color, size=(10,0),key='-CPU0-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU0-')],
    #[pysg.Text('CPU1:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU1-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU1-')],
    #[pysg.Text('CPU2:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU2-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU2-')],
    #[pysg.Text('CPU3:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU3-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU3-')],
    #[pysg.Text('CPU4:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU4-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU4-')],
    #[pysg.Text('CPU5:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU5-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU5-')],
    #[pysg.Text('CPU6:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU6-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU6-')],
    #[pysg.Text('CPU7:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU7-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU7-')],
    #[pysg.Text('CPU8:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU8-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU8-')],
    #[pysg.Text('CPU9:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU9-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU9-')],
    #[pysg.Text('CPU10:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU10-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU10-')],
    #[pysg.Text('CPU11:')],
    [pysg.Text('', text_color=font_color, size=(10,0),key='-CPU11-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU11-')],  
]

layout_memoria = [
    [pysg.Text('Memória RAM Total:')],
    [pysg.Text(f'{mem_total}GB', text_color=font_color, size=(20,0), )],
    [pysg.Text('Utilizada:')],
    [pysg.Text('', text_color=font_color, size=(20,0), key='-MEMORIA-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,20), key='-PROGMEM-')]
]

layout_disco = [
    [pysg.Text('Capacidade Total: ')],
    [pysg.Text(f'{disco_total}GB', text_color=font_color)],
    [pysg.Text('Utilizado:')],
    [pysg.Text('', text_color=font_color, size=(20,0), key='-DISCO-')],
    [pysg.ProgressBar(100, orientation='h', size=(30,20), key='-PROGDISC-')]
]

layout_rede = [
    [pysg.Text('IPv4:')],
    [pysg.Text(f'{ip}', text_color=font_color)],
    [pysg.Text('IPv6:')],
    [pysg.Text(f'{ipv6}', text_color=font_color)],
    [pysg.Text('Endereço físico:')],
    [pysg.Text(f'{physical_address}', text_color=font_color)]
]

#Carrega dados no layout_diretorios com o dirFinder()
layout_diretorios = [
    [pysg.Text('Mapeamento de diretórios na raiz do Python:')]
]

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
    layout_diretorios.append([pysg.Text(f'{linhaRes}', text_color=font_color)])
    print("     (CHAMADA) ", time.ctime(), nome)
# dirFinder()

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
    layout_processos.append([pysg.Text(f'{linhaRes}', text_color=font_color)])
    print("     (CHAMADA) ", time.ctime(), nome)
# pidFinder()


#Escalonamento de chamadas com sched
scheduler = sched.scheduler(time.time, time.sleep)

def print_event(nome):
    print("EVENTO:", time.ctime(), nome)

scheduler.enter(3, 1, dirFinder, ("- INFO: Função de  diretórios",))
scheduler.enter(6, 1, pidFinder, ("- INFO: Função de  PID's\n",))
print("\nINÍCIO DE ESCALONAMENTO DE CHAMADAS:", time.ctime(),"\n")

t0 = time.perf_counter()
freq_cpu1 = str(round(psutil.cpu_freq().current, 2))
scheduler.run()
sec = round(time.perf_counter() - t0)
print("Tempo de processo do Scheduler antes de iniciar a aplicação = "+str(sec)+" segundos.") 
print("Ciclos do procesador (Frequència ou Clock) utilizados = " + freq_cpu1 + " milhões de hertz por segundo.\n")


#Definição de layout com Tabs
abas = [
    [pysg.TabGroup([
        [
            pysg.Tab('Geral', layout_geral),
            pysg.Tab('CPU', layout_cpu),
            pysg.Tab('Threds', layout_threads),
            pysg.Tab('Memória', layout_memoria),
            pysg.Tab('Disco', layout_disco),
            pysg.Tab('Rede', layout_rede),
            pysg.Tab('Diretórios', layout_diretorios),
            pysg.Tab('Processos', layout_processos)
            ]], tab_location='left', selected_background_color='Gray', border_width=5)
        ],
        [pysg.Text('', size=(36,0)), pysg.Button('Home'), pysg.Button('Fechar')]
]

#Definição de Window
window = pysg.Window('System Information', abas)

while True:
    event, values = window.read(timeout=10)
    
    if (event == pysg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Fechar') and pysg.popup_yes_no('Deseja mesmo sair?') == 'Yes':
        break
    if event == 'Home':
        window['Geral'].select()
        
    uso_cpu = psutil.cpu_percent(interval=1)
    freq_cpu = str(round(psutil.cpu_freq().current, 2))
    mem = psutil.virtual_memory()
    porcent_memoria = mem.percent
    cores_info = psutil.cpu_percent(interval=1, percpu=True)

    window['-USOCPU-'].update(f'{uso_cpu}%')
    window['-FREQCPU-'].update(f'{freq_cpu} MHz')
    window['-PROGCPU-'].update(uso_cpu)

    window['-CPU0-'].update(f'CPU0: {cores_info[0]}%')
    window['-PROGCPU0-'].update(cores_info[0])
    window['-CPU1-'].update(f'CPU1: {cores_info[1]}%')
    window['-PROGCPU1-'].update(cores_info[1])
    window['-CPU2-'].update(f'CPU2: {cores_info[2]}%')
    window['-PROGCPU2-'].update(cores_info[2])
    window['-CPU3-'].update(f'CPU3: {cores_info[3]}%')
    window['-PROGCPU3-'].update(cores_info[3])
    window['-CPU4-'].update(f'CPU4: {cores_info[4]}%')
    window['-PROGCPU4-'].update(cores_info[4])
    window['-CPU5-'].update(f'CPU5: {cores_info[5]}%')
    window['-PROGCPU5-'].update(cores_info[5])
    window['-CPU6-'].update(f'CPU6: {cores_info[6]}%')
    window['-PROGCPU6-'].update(cores_info[6])
    window['-CPU7-'].update(f'CPU7: {cores_info[7]}%')
    window['-PROGCPU7-'].update(cores_info[7])
    window['-CPU8-'].update(f'CPU8: {cores_info[8]}%')
    window['-PROGCPU8-'].update(cores_info[8])
    window['-CPU9-'].update(f'CPU9: {cores_info[9]}%')
    window['-PROGCPU9-'].update(cores_info[9])
    window['-CPU10-'].update(f'CPU10: {cores_info[10]}%')
    window['-PROGCPU10-'].update(cores_info[10])
    window['-CPU11-'].update(f'CPU11: {cores_info[11]}%')
    window['-PROGCPU11-'].update(cores_info[11])

    window['-MEMORIA-'].update(f'{porcent_memoria}%')
    window['-PROGMEM-'].update(porcent_memoria)
    window['-DISCO-'].update(f'{percent_disco}%')
    window['-PROGDISC-'].update(percent_disco)

window.close()