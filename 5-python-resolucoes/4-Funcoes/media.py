def media(primeiraNota, segundaNota, terceiraNota, letra: str):
    if letra.upper().__eq__('A'):
        return (primeiraNota + segundaNota + terceiraNota) / 3
    elif letra.upper().__eq__('P'):
        return ((primeiraNota * 5) + (segundaNota * 3) + (terceiraNota * 2)) / 10
    else:
        return 0
    

print(media(3, 4, 5, 'P'))