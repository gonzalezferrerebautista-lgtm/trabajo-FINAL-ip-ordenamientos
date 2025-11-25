# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
# Usamos merges que insertan el elemento de la derecha en la izquierda
# mediante swaps adyacentes (uno por micro-paso) para que el visualizador
# que solo sabe hacer swaps pueda representar los movimientos.
width = 1    # tamaño de bloque
left = 0     # inicio del bloque actual
mid = 0      # fin del primer sub-bloque
right = 0    # fin del segundo sub-bloque
i = 0        # cursor izquierdo 
j = 0        # cursor derecho 
phase = 'start'   
shifting_k = None 

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)
    
    global width, left, mid, right, i, j, phase, shifting_k
    width = 1
    left = 0
    mid = 0
    right = 0
    i = 0
    j = 0
    phase = 'start'
    shifting_k = None

def step():
    # mergear bloques adyacentes [left..mid] y [mid+1..right].
    # Cuando un elemento del segundo bloque debe insertarse antes de uno
    # del primer bloque, lo desplazamos hacia la izquierda mediante swaps
    # adyacentes (uno por micro-paso). Esto permite reutilizar la lógica
    # de visualización que solo ejecuta swaps entre dos índices.

    global items, n, width, left, mid, right, i, j, phase, shifting_k

    if n <= 1:
        return {"done": True}

    # Si ya llegamos a width >= n
    if width >= n:
        return {"done": True}

    # Buscar el siguiente bloque para mergear
    while True:
        if phase == 'start':
            if left >= n:
                # fin de la pasada -> duplicar block size y reiniciar
                width *= 2
                left = 0
                if width >= n:
                    return {"done": True}
                # continuar buscando un bloque
                continue

            mid = min(left + width - 1, n - 1)
            right = min(left + 2 * width - 1, n - 1)
            if mid >= right:
                # no hay segundo bloque -> saltar
                left += 2 * width
                continue
            # inicializar cursores para este merge
            i = left
            j = mid + 1
            shifting_k = None
            phase = 'compare'

        # decidir si avanzamos i o empezamos a desplazar j
        if phase == 'compare':
            # Si ya consumimos alguno de los runs
            if i > mid or j > right:
                # pasar al siguiente bloque
                a = min(max(left, 0), n - 1)
                b = a
                left += 2 * width
                phase = 'start'
                return {"a": a, "b": b, "swap": False, "done": False}

            a = i
            b = j
            # Si el elemento izquierdo es menor o igual, avanzamos i
            if items[i] <= items[j]:
                i += 1
                return {"a": a, "b": b, "swap": False, "done": False}
            else:
                # hay que insertar items[j] en la posición i
                shifting_k = j
                phase = 'shifting'
                # realizamos un único swap adyacente
                items[shifting_k - 1], items[shifting_k] = items[shifting_k], items[shifting_k - 1]
                new_k = shifting_k - 1
                # si llegamos a i, la inserción terminó
                if new_k == i:
                    # ajustar punteros: el primer run creció en 1
                    shifting_k = None
                    i += 1
                    mid += 1
                    j += 1
                    phase = 'compare'
                else:
                    shifting_k = new_k
                    phase = 'shifting'
                return {"a": new_k, "b": new_k + 1, "swap": True, "done": False}

        # seguimos moviendo el elemento desde la derecha hacia la izquierda
        if phase == 'shifting':
            # shifting_k apunta al índice actual del elemento que estamos moviendo
            if shifting_k is None:
                phase = 'compare'
                continue
            # hacemos un swap entre shifting_k-1 y shifting_k
            if shifting_k - 1 < 0:
                phase = 'compare'
                continue
            items[shifting_k - 1], items[shifting_k] = items[shifting_k], items[shifting_k - 1]
            new_k = shifting_k - 1
            # Si llegamos a i, terminamos la inserción
            if new_k == i:
                shifting_k = None
                i += 1
                mid += 1
                j += 1
                phase = 'compare'
            else:
                shifting_k = new_k
                phase = 'shifting'
            return {"a": new_k, "b": new_k + 1, "swap": True, "done": False}

    return {"done": True}
