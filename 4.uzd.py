fails = input("Ievadi faila nosaukumu: ")
try: 
    with open(fails, 'r', encoding='utf-8') as g:
        print(g.read())
except FileNotFoundError:
    print("Šāds fails nav atrasts")

