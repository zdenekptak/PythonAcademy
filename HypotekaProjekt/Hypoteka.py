def main():
    vstUdajeKHypo = vstupniInformace()
    pujcka = vstUdajeKHypo[0]
    urok = vstUdajeKHypo[1]
    pocetMesicu = vstUdajeKHypo[2] * 12

    splatka = mesicniSplatka(pujcka, urok, pocetMesicu)

def vstupniInformace():
    # Vyse pujcky
    castka = float(input("Kolik si chcete pujcit: "))
    # Urok
    urok = float(input("Jaký chcete úrok: "))
    # Delka splatky v letech
    roky = int(input("Na kolik let si chcete pujcit: "))
    # Odradkovani
    print()
    # Vraceni vstupů
    return [castka, urok, roky]

def mesicniSplatka(pujcka, urok, pocetMesicu):
    r = urok / 100 / 12
    mesicniSplatka = pujcka*(r * (1 + r)**pocetMesicu) / ((1 + r)**pocetMesicu-1)
    return mesicniSplatka