waga_elementu = int(input())
waga_paczki = 0
wyslane_paczki = 0
waga_ostatniego_elementu = 0
suma_pustych_kg = 0
puste_kg = 0
razem_kg = 0

while waga_elementu > 0 and waga_elementu <= 10:
    waga_paczki += waga_elementu

    if waga_paczki < 20:
        print("Dobieram element")
        # waga_ostatniego_elementu = waga_paczki

    elif waga_paczki == 20:
        print("Idealnie! Wysyłam")
        razem_kg += waga_paczki
        puste_kg = 20 - waga_paczki
        suma_pustych_kg += puste_kg
        wyslane_paczki = wyslane_paczki + 1
        waga_paczki = 0
        # waga_ostatniego_elementu = 0

    else:
        print("Maksymalna waga paczki przekroczona! Odejmuję element i wysyłam")
        waga_paczki -= waga_elementu
        wyslane_paczki = wyslane_paczki + 1
        puste_kg = 20 - waga_paczki
        suma_pustych_kg += puste_kg
        razem_kg += waga_paczki
        waga_paczki = waga_elementu
        # waga_ostatniego_elementu = waga_elementu