# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0
g = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def init(vals):
    global items, n, i, j, g
    items = list(vals)
    n = len(items)
    # TODO: inicializar punteros/estado
    # Variables para la versión paso-a-paso de Shell sort
    # `gap` será la distancia entre elementos comparados; usamos `g` como alias
    # inicial: gap = n//2
    if n <= 1:
        g = 0
    else:
        g = n // 2
    i = g
    j = None


def step():
    global items, n, i, j, g

    # Si gap/ g es 0 o menor, ya estamos ordenados
    if not g or g <= 0:
        return {"done": True}

    # Si i es None o i >= n, significa que debemos reducir gap
    if i is None or i >= n:
        # reducir gap
        g //= 2
        if g <= 0:
            return {"done": True}
        i = g
        j = None
        # devolvemos un paso neutro para que la UI refresque
        a = 0
        b = 0
        return {"a": a, "b": b, "swap": False, "done": False}

    # Si j es None: inicializar el cursor interno para la posición i
    if j is None:
        j = i
        a = j - g
        b = j
        return {"a": a, "b": b, "swap": False, "done": False}

    # Comparar items[j-g] con items[j]
    a = j - g
    b = j
    if a < 0 or b < 0 or a >= n or b >= n:
        # índices fuera de rango; avanzar
        i += 1
        j = None
        return {"a": 0, "b": 0, "swap": False, "done": False}

    if items[a] > items[b]:
        # hacer un único swap adyacente (según gap)
        items[a], items[b] = items[b], items[a]
        # después del swap, avanzamos j hacia la izquierda en el run
        j -= g
        # si j queda por debajo de gap, terminamos el inner-loop
        if j < g:
            i += 1
            j = None
        return {"a": a, "b": b, "swap": True, "done": False}
    else:
        # no hay swap: avanzar i y reiniciar j
        i += 1
        j = None
        return {"a": a, "b": b, "swap": False, "done": False}
