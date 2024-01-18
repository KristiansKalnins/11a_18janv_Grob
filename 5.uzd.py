dati = input('Ievadi savu vārdu un uzvārdu: ')
try:
    with open ("lietotajs.txt", 'w', encoding='utf-8') as we:
     we.write(dati)
except FileNotFoundError:
    print("Šāds fails nav atrasts")
except FileExistsError:
    print('Sāds fails jau eksistē')
