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