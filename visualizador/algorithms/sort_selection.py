# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # puntero inicial de la pasada actual
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    # TODO:
    global items, n, i, j, min_idx, fase

    
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j
    if fase=="buscar": 
        
        if (items[j]<items[min_idx]) :
            min_idx=j
        a= min_idx
        b= j
        j+=1
        
        if j>=n:
            fase="swap"

    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
        return {"a": a, "b": b, "swap": False, "done": False}
    
    #   Al terminar el barrido, pasar a fase "swap".
    

    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    if fase=="swap":
        if min_idx != i:
            items[i],items[min_idx]=items[min_idx],items[i]
            a=i
            b=min_idx
        else:
            a = i
            b = i 
        #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
        i+=1
        j=i+1
        min_idx=i
        fase="buscar"
        return {"a": a, "b": b, "swap": True, "done": False}
    
    # Cuando i llegue al final, devolvé {"done": True}.
    if i >= n-1:
        return {"done": True}
    
    
