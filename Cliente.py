#Código baseado com internet cabeada (Ethernet), processador com 12 threads e sistema operacional Windows.
#Provavelmente será necessária a adaptação dessas variáveis para funcionamento correto em outras máquinas e sistemas.

import PySimpleGUI as pysg
import psutil

#Chama o cliente com os dados vindos do servidor
from utils.ClienteService import ClientData

#Setando tema e cor de fonte do sistema
pysg.theme('LightBrown13') #Banco de temas pode ser encontrado aqui: https://user-images.githubusercontent.com/46163555/71361827-2a01b880-2562-11ea-9af8-2c264c02c3e8.jpg
font_color = 'Black'

#Dados de memória
mem = psutil.virtual_memory()
porcent_memoria = mem.percent
#texto_memoria = str(mem_total) + "GB / " + str(porcent_memoria) + "%"

#Dados de disco
disco = psutil.disk_usage(".")
percent_disco = disco.percent
# texto_uso_disco = "(Total: " + str(disco_total) + "GB / " + str(percent_disco) + "%)"

#Layout de abas
layout_geral = [] #Vem do servidor
layout_cpu = [] #Vem do servidor (com excessão do dado atualizado em tempo real)
layout_threads = [] # Vem do local pois são atualizados em tempo real
layout_memoria = [] #Vem do servidor (com excessão do dado atualizado em tempo real)
layout_disco = [] #Vem do servidor (com excessão do dado atualizado em tempo real)
layout_rede1 = [] #Vem do servidor
layout_rede2 = [] #Vem do servidor
layout_diretorios = [] #Vem do servidor
layout_processos = [] #Vem do Servidor
layout_sched = [] #Vem do servidor

#Aquisição de dados do servidor
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
    # Disco
    layout_disco.append([pysg.Text('Capacidade total do disco onde este projeto está localizado: ')])      
    layout_disco.append([pysg.Text(tabela[6][0], text_color=font_color)])
    layout_disco.append([pysg.Text('Utilizado:')])
    layout_disco.append([pysg.Text('', text_color=font_color, size=(20,0), key='-DISCO-')]) #Vem do local (tempo real)
    layout_disco.append([pysg.ProgressBar(100, orientation='h', size=(30,20), key='-PROGDISC-')]) #Vem do local (tempo real)
    # Memória
    layout_memoria.append([pysg.Text('Memória RAM Total:')])
    layout_memoria.append([pysg.Text(tabela[7][0], text_color=font_color, size=(20,0), )])
    layout_memoria.append([pysg.Text('Utilizada:')])
    layout_memoria.append([pysg.Text('', text_color=font_color, size=(20,0), key='-MEMORIA-')])
    layout_memoria.append([pysg.ProgressBar(100, orientation='h', size=(30,20), key='-PROGMEM-')])
    # CPU
    layout_cpu.append([pysg.Text('Marca do processador:')])
    layout_cpu.append([pysg.Text(tabela[8][0], text_color=font_color)])
    layout_cpu.append([pysg.Text('Núcleos físicos:')])
    layout_cpu.append([pysg.Text(tabela[8][1], text_color=font_color)])
    layout_cpu.append([pysg.Text('Núcleos lógicos:')])
    layout_cpu.append([pysg.Text(tabela[8][2], text_color=font_color)])
    layout_cpu.append([pysg.Text('Frequência total:')])
    layout_cpu.append([pysg.Text('', text_color=font_color, size=(10,0),key='-FREQCPU-')])
    layout_cpu.append([pysg.Text('Uso de CPU (Total):')])
    layout_cpu.append([pysg.Text('', text_color=font_color, size=(10,0),key='-USOCPU-')])
    layout_cpu.append([pysg.ProgressBar(100, orientation='h', size=(30,20), key='-PROGCPU-')])
    # Threads
    #[pysg.Text('CPU0:')],
    layout_threads.append([pysg.Text('CPU0', text_color=font_color, size=(10,0),key='-CPU0-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU0-')])
    #[pysg.Text('CPU1:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU1-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU1-')])
    #[pysg.Text('CPU2:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU2-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU2-')])
    #[pysg.Text('CPU3:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU3-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU3-')])
    #[pysg.Text('CPU4:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU4-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU4-')])
    #[pysg.Text('CPU5:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU5-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU5-')])
    #[pysg.Text('CPU6:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU6-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU6-')])
    #[pysg.Text('CPU7:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU7-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU7-')])
    #[pysg.Text('CPU8:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU8-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU8-')])
    #[pysg.Text('CPU9:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU9-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU9-')])
    #[pysg.Text('CPU10:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU10-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU10-')])
    #[pysg.Text('CPU11:')],
    layout_threads.append([pysg.Text('', text_color=font_color, size=(10,0),key='-CPU11-')])
    layout_threads.append([pysg.ProgressBar(100, orientation='h', size=(30,5), key='-PROGCPU11-')])
serverDataFinder()

print("* * * * * INFO: Aplicação inicializada. * * * * *\n")

#Definição de abas
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

#Estrutura de funcionamento da aplicação em Run
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