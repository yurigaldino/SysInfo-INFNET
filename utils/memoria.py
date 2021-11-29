import psutil

#Dados de memória
mem = psutil.virtual_memory()
mem_total = round(mem.total / pow(2, 30), 2)

layout_memoria = []

def dataMemoria():
    layout_memoria.append(f'{mem_total} GB')

    return layout_memoria