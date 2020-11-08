# produkty = ["mleko", "bulka", "mieso", "sok", "arbuz", "szafa"]
# ceny = [4, 1, 20, 5, 6, 505]
produkty = ["mleko", "bulka"]
ceny = [4, 1]

produkt_cena = dict(zip(produkty, ceny))


def paragon(koszyk):
    do_zaplaty = sum(produkt_cena.values())
    ilosc_prod_w_koszyku = len(produkt_cena)
    # print(min(produkt_cena.values()))

    if ilosc_prod_w_koszyku > 3 and do_zaplaty < 500:
        do_zaplaty = round(do_zaplaty*0.95,2)


    if do_zaplaty >= 500 and ilosc_prod_w_koszyku >= 2:
        do_zaplaty = round(do_zaplaty*0.90,2)

    else:
        do_zaplaty = do_zaplaty

    return do_zaplaty



koszyk = paragon(produkt_cena)
print(koszyk)
