def sumaHasta(n):
    if n == 1:
        return 1
    else:
        return n + sumaHasta(n - 1)
    
sumaHasta(0)