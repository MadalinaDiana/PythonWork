jucatori = ['Madalina', 'Arthur', 'Meli', 'Nandi', 'Gimi']
rezerve = ['Mihai', 'Iustin', 'Luca', 'Andreea', 'Germi']
jucatori_scosi = []
print(f'Lista cu jucatori este: {jucatori}')
print(f'Lista cu rezerve este: {rezerve}')

schimbari_max = 0
while schimbari_max < 3:
    jucator_de_sters, jucator_de_adaugat = input("Introdu numele jucatorului pe care doresti sa il SCHIMBI: "), \
                                           input("Introdu numele jucatprului de rezerva pe care vrei sa il adaugi: ")
    # if jucator_de_sters in jucatori_scosi or jucator_de_adaugat in jucatori_scosi:
    #     print(f'Nu se poate efectua schimbarea deoarece jucătorul trebuie sa se odihneasca')
    # elif jucator_de_sters not in jucatori or jucator_de_adaugat not in rezerve:
    #     print(f'Nu se poate efectua schimbarea deoarece jucătorul nu e în teren')
    # else:
    #     jucatori_scosi.append(jucator_de_sters)
    #     jucatori.remove(jucator_de_sters)
    #     rezerve.remove(jucator_de_adaugat)
    #     jucatori.append(jucator_de_adaugat)
    #     print(f'---------------------------------------')
    #     print(f'Noua lista cu jucatori este: {jucatori}')
    #     print(f'Noua lista cu rezerve este: {rezerve}')
    #     print(f'---------------------------------------')
    #     print(f'A intrat {jucator_de_adaugat} si a iesit {jucator_de_sters}')
    #     print(f'Noua lista cu jucatori scosi pana la finalul meciului este: {jucatori_scosi}')
    #     schimbari_max = schimbari_max + 1
    #     print(f'Mai ai schimbari de efectuat maxim: {3 - schimbari_max}')

    if jucator_de_sters in jucatori and jucator_de_adaugat in rezerve:
        jucatori_scosi.append(jucator_de_sters)
        jucatori.remove(jucator_de_sters)
        rezerve.remove(jucator_de_adaugat)
        jucatori.append(jucator_de_adaugat)
        print(f'---------------------------------------')
        print(f'Noua lista cu jucatori este: {jucatori}')
        print(f'Noua lista cu rezerve este: {rezerve}')
        print(f'---------------------------------------')
        print(f'A intrat {jucator_de_adaugat} si a iesit {jucator_de_sters}')
        print(f'Noua lista cu jucatori scosi pana la finalul meciului este: {jucatori_scosi}')
        schimbari_max = schimbari_max + 1
        print(f'Mai ai schimbari de efectuat maxim: {3 - schimbari_max}')
    else:
        print("Nu se poate efectua schimbarea")