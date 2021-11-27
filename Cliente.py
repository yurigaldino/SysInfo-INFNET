#Código baseado com internet cabeada (Ethernet), processador com 12 threads e sistema operacional Windows.
#Provavelmente será necessária a adaptação dessas variáveis para funcionamento correto em outras máquinas e sistemas.

import PySimpleGUI as pysg
import psutil, platform

#Chama o cliente com os dados vindos do servidor
from utils.ClienteService import ClientData

#Setando tema e cor de fonte do sistema
pysg.theme('LightBrown13') #Banco de temas pode ser encontrado aqui: https://user-images.githubusercontent.com/46163555/71361827-2a01b880-2562-11ea-9af8-2c264c02c3e8.jpg
font_color = 'Black'

#Dados de sistema
marca = str(platform.processor())

#Dados de processador
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

#Layout de abas
layout_geral = []

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

layout_rede1 = [] #Vem do servidor

layout_rede2 = [] #Vem do servidor

layout_diretorios = [] #Vem do servidor

layout_processos = [] #Vem do Servidor

layout_sched = [] #Vem do servidor

def serverDataFinder():
    tabela = ClientData()
    # Rede 2
    for i in tabela[0]:
        layout_rede2.append([pysg.Text(i, text_color=font_color)])
    # Sched
    layout_sched.append([pysg.Text('Utilização do módulo Scheduler para escalonamento com medição de tempo e comparação da quantidade total de')])
    layout_sched.append([pysg.Text('clocks utilizados pela CPU:')])
    for i in tabela[1]:
        layout_sched.append([pysg.Text(i, text_color=font_color)])
    # Diretórios
    layout_diretorios.append([pysg.Text('Mapeamento de diretórios na raiz do Projeto:')])
    for i in tabela[2]:
        layout_diretorios.append([pysg.Text(i, text_color=font_color)])
    # Processos
    layout_processos.append([pysg.Text("PID    #    Threads   #   Criação    #    T. Usu    #    T. Sis    #    Mem. (%)    #    RSS    #    VMS    #    Executável:")])
    for i in tabela[3]:        
        layout_processos.append([pysg.Text(i, text_color=font_color)])
    # Geral
    layout_geral.append([pysg.Text('SO:')])      
    layout_geral.append([pysg.Text(tabela[4][0], text_color=font_color)])
    layout_geral.append([pysg.Text('Versão do SO:')])
    layout_geral.append([pysg.Text(tabela[4][1], text_color=font_color)])
    layout_geral.append([pysg.Text('Nome da máquina:')])
    layout_geral.append([pysg.Text(tabela[4][2], text_color=font_color)])
    layout_geral.append([pysg.Text('Arquitetura:')])
    layout_geral.append([pysg.Text(tabela[4][3], text_color=font_color)])
    layout_geral.append([pysg.Text('Palavra da CPU:')])
    layout_geral.append([pysg.Text(tabela[4][4], text_color=font_color)])
    # Rede 1
    layout_rede1.append([pysg.Text('IPv4:')])      
    layout_rede1.append([pysg.Text(tabela[5][0], text_color=font_color)])
    layout_rede1.append([pysg.Text('IPv6:')])
    layout_rede1.append([pysg.Text(tabela[5][1], text_color=font_color)])
    layout_rede1.append([pysg.Text('Endereço físico:')])
    layout_rede1.append([pysg.Text(tabela[5][2], text_color=font_color)])

serverDataFinder()

print("* * * * * INFO: Aplicação inicializada. * * * * *\n")

abas = [
    [pysg.TabGroup([
        [
            pysg.Tab('Geral', layout_geral),
            pysg.Tab('CPU', layout_cpu),
            pysg.Tab('Threds', layout_threads),
            pysg.Tab('Memória', layout_memoria),
            pysg.Tab('Disco', layout_disco),
            pysg.Tab('Rede I', layout_rede1),
            pysg.Tab('Rede II', layout_rede2),
            pysg.Tab('Diretórios', layout_diretorios),
            pysg.Tab('Processos', layout_processos),
            pysg.Tab('Scheduler', layout_sched)
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