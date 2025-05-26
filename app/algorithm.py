def dda_algorithm(xUno, yUno, xDos, yDos):
    if (xUno > xDos) or (xUno == xDos and yUno > yDos):
        xUno, xDos = xDos, xUno
        yUno, yDos = yDos, yUno

    tabla = []
    dx = xDos - xUno
    dy = yDos - yUno

    pasos = max(abs(dx), abs(dy))  
    x_inc = dx / pasos
    y_inc = dy / pasos

    x = xUno
    y = yUno

    for i in range(pasos + 1):
        tabla.append([round(x), round(y)])
        x += x_inc
        y += y_inc
    return tabla

def brhm(xUno, yUno, xDos, yDos):
    if (xUno > xDos) or (xUno == xDos and yUno > yDos):
        xUno, xDos = xDos, xUno
        yUno, yDos = yDos, yUno

    tabla = []
    dx = xDos - xUno
    dy = yDos - yUno
    ddy = 2 * dy
    ddyx = (2 * dy) - (2 * dx)

    x = xUno
    y = yUno
    p = (2 * dy) - dx

    for i in range(dx + 1):
        tabla.append([round(x), round(y)])
        x += 1
        if p < 0:
            p += ddy
        else:
            y += 1
            p += ddyx

    return tabla


def cir (x,y,radio):
    tabla = []
    dx = radio
    dy = 0
    p = 1 - radio

    while dx >= dy:
        tabla.append([dx,dy])
        dx = (dx if p <= 0 else dx - 1)
        dy = (dy + 1)
        p  = p + (2 * tabla[-1][1]+ 1)  if p <= 0 else p + ((2 * tabla[-1][1])-(2 * tabla[-1][0])) + 1


    for i in range(len(tabla)):
        tabla[i][0] += x
        tabla[i][1] += y

    nuevatabla = []
    for fila in tabla:
        x = fila[0]
        y = fila[1]
        
        nuevatabla.append([x, y])
        nuevatabla.append([-x, y])
        nuevatabla.append([x, -y])
        nuevatabla.append([-x, -y])
        nuevatabla.append([y, x])
        nuevatabla.append([-y, x])
        nuevatabla.append([y, -x])
        nuevatabla.append([-y, -x])

    resultado = tabla + nuevatabla

    return resultado

def elip (a,b,h,k):
    tabla = []
    x = 0
    y = b
    p = (b**2) - (a**2 * b) + (a**2) / 4

    while (2*b**2*x) <= (2*a**2*y):
        tabla.extend([
            [x + h,  y + k],
            [-x + h, y + k],
            [x + h, -y + k],
            [-x + h, -y + k]
        ])
        if p < 0:
            p = p + (2 * (b**2) * (x+1))
        else:
            p = p + (2 * (b**2) * (x+1)) - (2 * (a**2) * (y-1))
            y = y - 1
        x = x + 1
    
    p2 = (b**2 * (x + 0.5)*2) + (a**2 * (y - 1)*2) - (a**2 * b**2)
    while y >= 0:
        tabla.extend([
            [x + h,  y + k],
            [-x + h, y + k],
            [x + h, -y + k],
            [-x + h, -y + k]
        ])
        if p2 > 0:
            p2 =  p2 - (2 * a**2 * (y - 1))
        else:
            p2 = p2 - (2 * a**2 * (y - 1)) + (2 * b**2 * (x + 1))
            x = x + 1.
        
        y = y - 1

    return tabla