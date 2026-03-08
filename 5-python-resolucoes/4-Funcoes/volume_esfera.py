def volume_esfera(r):
    v = ((4 * 3.14) * (r ** 3)) / 3
    return format(v, '.2f')

print(volume_esfera(4))