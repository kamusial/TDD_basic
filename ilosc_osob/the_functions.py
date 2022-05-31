def ile_osob(dl, szer, pietra):
    if isinstance(dl, (float, int)) and isinstance(szer, (float, int)) and isinstance(pietra, int) and dl > 0 and szer > 0 and pietra > 0:
        ilosc = dl * szer * pietra / 7.5
        return int(ilosc)
    else:
        return 0


def ile_ze_srodkami(ilosc_osob,srodki):
    if isinstance(ilosc_osob, int) and ilosc_osob > 0:
        if srodki == "T":
            return int(ilosc_osob * 1.1)
        elif srodki == "N":
            return int(ilosc_osob * 0.5)
        else:
            print('Nie rozpoznano opcji')
            return 0
    else:
        return 0