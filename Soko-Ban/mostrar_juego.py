def primer_pos(c,f):
    '''Devuelve True en la primer pos'''
    if c == 0 and not f == 0:
        return False
    if not c == 0 and f == 0:
        return False
    if c == 0 and f == 0:
        return True