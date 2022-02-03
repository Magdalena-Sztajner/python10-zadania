miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
szablon_podsumowanie_1 = "W {} pozostało do spłaty: "

do_splaty_sty22 = (1 + ((inflacja + oprocentowanie) / 1200)) * pozyczka - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
do_splaty_zaokr = round(do_splaty_sty22)
mniej_o = pozyczka - do_splaty_sty22
mniej_o_zaokr = round(mniej_o)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o_zaokr) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_lut22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_sty22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_sty22 - do_splaty_lut22)
do_splaty_zaokr = round(do_splaty_lut22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_mar22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_lut22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_lut22 - do_splaty_mar22)
do_splaty_zaokr = round(do_splaty_mar22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_kwi22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_mar22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_mar22 - do_splaty_kwi22)
do_splaty_zaokr = round(do_splaty_kwi22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_maj22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_kwi22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_kwi22 - do_splaty_maj22)
do_splaty_zaokr = round(do_splaty_maj22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_cze22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_maj22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_maj22 - do_splaty_cze22)
do_splaty_zaokr = round(do_splaty_cze22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200

do_splaty_lip22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_cze22 - rata

podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_cze22 - do_splaty_lip22)
do_splaty_zaokr = round(do_splaty_lip22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_sie22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_lip22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_lip22 - do_splaty_sie22)
do_splaty_zaokr = round(do_splaty_sie22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_wrz22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_sie22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_sie22 - do_splaty_wrz22)
do_splaty_zaokr = round(do_splaty_wrz22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_paz22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_wrz22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_wrz22 - do_splaty_paz22)
do_splaty_zaokr = round(do_splaty_paz22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_lis22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_paz22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_paz22 - do_splaty_lis22)
do_splaty_zaokr = round(do_splaty_lis22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

miesiac = input()
inflacja = float((input()))
oprocentowanie = 3
pozyczka = 12000
rata = 200
do_splaty_gru22 = (1 + ((inflacja + oprocentowanie) / 1200)) * do_splaty_lis22 - rata
podsumowanie_1 = szablon_podsumowanie_1.format(miesiac)
mniej_o = round(do_splaty_lis22 - do_splaty_gru22)
do_splaty_zaokr = round(do_splaty_gru22)
print((podsumowanie_1 + str(do_splaty_zaokr)) + " zł" ", " + "to mniej o " + str(mniej_o) + " zł niż miesiąc temu.")

