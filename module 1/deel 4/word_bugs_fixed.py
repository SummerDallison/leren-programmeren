a = input('Geef een woord ')
b = input('Geef nog een woord ')

if len(a) > len(b):     
    print(f'{a} heeft meer letters dan woord {b}')
elif len(a) < len(b):   
    print(f'{a} heeft minder letters dan {b}')
else:                   
    print(f'{a} en {b} hebben evenveel letters')