# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # contador de vueltas actual
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo
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

    if n <= 1:
        return {"done": True}
    
    # Si ya terminamos todas las vueltas
    if i >= n - 1:
        return {"done": True}
    
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j
    if fase == "buscar": 
        if j < n:
            if items[j] < items[min_idx]:
                min_idx = j
            a = min_idx
            b = j
            j += 1
            # Si terminamos pasar a fase "swap"
            if j >= n:
                fase = "swap"
            return {"a": a, "b": b, "swap": False, "done": False}
        else:
            # Asegurar transición a swap si no hay más elementos
            fase = "swap"
            return {"a": min_idx, "b": min_idx, "swap": False, "done": False}
    
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    if fase == "swap":
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            a = i
            b = min_idx
            swap = True
        else:
            a = i
            b = i 
            swap = False
        # Preparar la siguiente vuelta
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        return {"a": a, "b": b, "swap": swap, "done": False}
    
    return {"done": True}
    
    
