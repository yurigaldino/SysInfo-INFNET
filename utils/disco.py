import psutil

#Dados de disco
disco = psutil.disk_usage(".")
disco_total = round(disco.total / pow(2, 30), 2)

layout_disco = []

def dataDisco():
    layout_disco.append(f'{disco_total} GB')

    return layout_disco