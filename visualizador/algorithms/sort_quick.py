items = []
n = 0
stack = []      
left = 0        
right = 0       
pivot_val = 0   # pivote
i = 0           # cursor izquierdo durante partición
j = 0           # cursor derecho durante partición
phase = 'init'  

def init(vals):
    global items, n, stack, left, right, pivot_val, i, j, phase
    items = list(vals)
    n = len(items)
    if n > 1:
        stack = [(0, n - 1)]
    else:
        stack = []
    phase = 'init'
    left = 0
    right = 0
    pivot_val = 0
    i = 0
    j = 0

def step():
    global items, n, stack, left, right, pivot_val, i, j, phase
    
    # Casos triviales
    if n <= 1:
        return {"done": True}
    
    # Si stack está vacío
    if not stack and phase == 'init':
        return {"done": True}
    
    # Fase 'init'
    if phase == 'init':
        if not stack:
            return {"done": True}
        left, right = stack.pop()
        if left >= right:
            # rango inválido
            return {"a": left, "b": left, "swap": False, "done": False}
        # elegir pivote
        pivot_val = items[right]
        i = left
        j = right - 1
        phase = 'scan_left'
        return {"a": left, "b": right, "swap": False, "done": False}
    
    # Fase 'scan_left': buscar elemento >= pivote desde la izquierda
    if phase == 'scan_left':
        if i <= j and items[i] < pivot_val:
            i += 1
            return {"a": i - 1, "b": i - 1, "swap": False, "done": False}
        else:
            phase = 'scan_right'
            return {"a": i, "b": i, "swap": False, "done": False}
    
    # Fase 'scan_right': buscar elemento <= pivote desde la derecha
    if phase == 'scan_right':
        if j >= i and items[j] >= pivot_val:
            j -= 1
            return {"a": j + 1, "b": j + 1, "swap": False, "done": False}
        else:
            if i < j:
                phase = 'swap'
            else:
                phase = 'finish_partition'
            return {"a": i, "b": j, "swap": False, "done": False}
    
    # Fase 'swap'
    if phase == 'swap':
        if i < j:
            items[i], items[j] = items[j], items[i]
            i += 1
            j -= 1
            phase = 'scan_left'
            return {"a": i - 1, "b": j + 1, "swap": True, "done": False}
        else:
            phase = 'finish_partition'
            return {"a": i, "b": j, "swap": False, "done": False}
    
    # Fase 'finish_partition'
    if phase == 'finish_partition':
        if i != right:
            items[i], items[right] = items[right], items[i]
        
        if i + 1 < right:
            stack.append((i + 1, right))
        if left < i - 1:
            stack.append((left, i - 1))
        
        phase = 'init'
        return {"a": i, "b": right, "swap": i != right, "done": False}
    
    return {"done": True}
