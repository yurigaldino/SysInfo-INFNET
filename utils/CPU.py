import psutil, platform

#Dados de sistema
marca = str(platform.processor())

#Dados de processador
cores_cpu = psutil.cpu_count(logical=False)
logical_cpu = psutil.cpu_count()

layout_cpu = []

def dataCPU():
    layout_cpu.append(f'{marca}')
    layout_cpu.append(f'{cores_cpu} cores')
    layout_cpu.append(f'{logical_cpu} threads')

    return layout_cpu