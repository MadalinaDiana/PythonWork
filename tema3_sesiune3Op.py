# meciul
jucatori = ['Madalina', 'Arthur', 'Meli', 'Nandi', 'Gimi']
print(jucatori)
schimbari_max = 0

while schimbari_max < 3:
    jucator_sters = input("Introdu numele jucatorului pe care doresti sa il schimbi: ")
    if jucator_sters not in jucatori:
        print(f'nu se poate efectua schimbarea deoarece jucătorul cu  nu e înteren')
    else:
        jucator_adaugat = input("Introdu numele jucatorului pe care doresti sa il adaugi: ")
        jucatori.remove(jucator_sters)
        jucatori.append(jucator_adaugat)
        print(f'Noua lista cu jucatori este: {jucatori}')
        print(f'A intrat {jucator_adaugat} si a iesit {jucator_sters}')
        schimbari_max = schimbari_max + 1
        print(f'Mai ai schimbari de efectuat maxim: {3-schimbari_max}')
print('S-a terminat meciul')
