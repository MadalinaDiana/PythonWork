import datetime
# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
def nrcomun(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3
# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.

def reducere(pret, discount):
    if 100 >= discount > 0:
        discount_amount = (discount * pret) / 100
        discounted_pret = (pret - discount_amount)
        print(f'Valoarea reducerii este: {discount_amount}, Pretul final redus pe care il platiti: {discounted_pret}')
    else:
        print('Reducerea este invalida, te rugam sa introduci o reducere intre 0 si 100')


"""3. Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)"""


def dataora(dt):
    dt_string = dt.strftime("Data: %d/%m/%Y  ora: %H:%M:%S")
    print("Data si ora curenta este =", dt_string)


# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)

def numOfDays(date1, date2):
    return (date2-date1).days


print(nrcomun([1, 1, 2, 3], [2, 2, 3, 4]))
reducere(500, 20)
dt = datetime.datetime.now()
dataora(dt)
date1 = datetime.date(2022, 9, 13)
date2 = datetime.date(2022, 10, 17)
print(numOfDays(date1, date2), "zile pana la data aleasa")


