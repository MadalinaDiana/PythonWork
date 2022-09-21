jucatori = ['Madalina', 'Arthur', 'Meli', 'Nandi', 'Gimi']
rezerve = ['Mihai', 'Iustin', 'Luca', 'Andreea', 'Germi']
jucatori_scosi = []
print(f'Lista cu jucatori este: {jucatori}')
print(f'Lista cu rezerve este: {rezerve}')

schimbari_max = 0

while schimbari_max < 3:
    jucator_sters = input("Introdu numele jucatorului pe care doresti sa il SCHIMBI: ")
    if jucator_sters in jucatori_scosi:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_sters} trebuie sa se odihneasca')
    elif jucator_sters not in jucatori:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator_sters} nu e în teren')
    else:
        jucator_adaugat = input("Introdu numele jucatorului de rezerva pe care doresti sa il ADAUGI: ")
        if jucator_adaugat in jucatori_scosi:
            print(f'nu se poate efectua schimbarea deoarece jucătorul {jucator_adaugat} trebuie sa se odihneasca')
        elif jucator_adaugat not in rezerve:
            print(f'nu se poate efectua schimbarea deoarece jucătorul {jucator_adaugat} nu este rezerva')
        else:
            jucatori_scosi.append(jucator_sters)
            jucatori.remove(jucator_sters)
            rezerve.remove(jucator_adaugat)
            jucatori.append(jucator_adaugat)
            print(f'---------------------------------------')
            print(f'Noua lista cu jucatori este: {jucatori}')
            print(f'Noua lista cu rezerve este: {rezerve}')
            print(f'---------------------------------------')
            print(f'A intrat {jucator_adaugat} si a iesit {jucator_sters}')
            print(f'Noua lista cu jucatori scosi pana la finalul meciului este: {jucatori_scosi}')
            schimbari_max = schimbari_max + 1
            print(f'Mai ai schimbari de efectuat maxim: {3 - schimbari_max}')
