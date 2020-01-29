temp = int(input('Temperatura: '))

if temp < 0:
    print("Está helado")
elif temp >= 0 and temp < 12:
    print("Hace mucho frío")
elif temp >= 12 and temp < 18:
    print("Hace frío")
elif temp >= 18 and temp < 24:
    print("Está calido")
elif temp >= 24:
    print("Hace calor")