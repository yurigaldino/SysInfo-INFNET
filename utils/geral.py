import PySimpleGUI as pysg
import psutil, platform, cpuinfo


marca = str(platform.processor())
nome = str(platform.node())
versao = str(platform.platform())
so = str(platform.system())
cpu_info = cpuinfo.get_cpu_info()
cores_cpu = psutil.cpu_count(logical=False)

layout_geral = []

def dataGeral():
    layout_geral.append(f'{so}')
    layout_geral.append(f'{versao}')
    layout_geral.append(f'{nome}')
    layout_geral.append(f'{cpu_info["arch"]}')
    layout_geral.append(f'{cpu_info["bits"]}')
    
    return layout_geral
