mesta = ["Praha", "Viden", "Brno", "Svitavy", "Zlin", "Ostrava"]
cena = [1000,1100,2000,1500,2300,3400]
mestasleva25 = ["Svitavy", "Ostrava"]
oddelovac = 80 * "="
pozdrav = 'Vítejte v místě, kde si lidé plánují výlety'



# Pozdrav klienta
print(oddelovac)
print(pozdrav)
print(oddelovac)
# Nabídni mu destinace

print("Můžeme nabídnut následující destinace:")
print(oddelovac)
print("""
1 - Prague  | 1000
2 - Wien    | 1100
3 - Brno    | 2000
4 - Svitavy | 1500
5 - Zlin    | 2300
6 - Ostrava | 3400
""")
print(oddelovac)
# Získej vstup uživatele o destinaci
cilovaDest = int(input("Zadej cislo cilove destinace: "))
print(oddelovac)

# Zkontroluj, zde byl vložen vhodný vstup
if cilovaDest < 1 or cilovaDest > len(mesta):
    print("Cilova destinace je zadana spatne")
    exit()
else:
    ciloveMesto = mesta[cilovaDest - 1]
    cena = cena[cilovaDest - 1]
    print("Cilova destinace je zadana spravne")
    if ciloveMesto in mestasleva25:
        print('Trefa! Získávaš 25% slevu na destinaci - ' + ciloveMesto)
        cena = cena * 0.75
        input(' Stiskni enter pro pokračování...')
    else:
        cena = cena

# Začni registraci
# Získej vstup uživatele o jeho osobních datech
print("Registrace:")
print("Abyste dokončili rezervaci, podělte se s námi o pár podrobností.")
print(oddelovac)
rok_narozeni = int(input("Zadej rok narozeni: "))
aktualni_rok = 2020
kontrola = aktualni_rok - rok_narozeni

if kontrola >= 15:
    print('Pokracuji')
    print(oddelovac)
else:
    print('Nase sluzby jsou az od 18 let.')
    exit()

jmeno = input("Zadej jmeno: ")
prijmeni = input("Zadej prijmeni: ")
if jmeno.isalpha() and prijmeni.isalpha():
    print(f"Jméno je v pořádku")
else:
    print("Vase jmeno a prijmeni je ve spatnem tvaru")
print(oddelovac)

email = input("Zadej email: ")
if "@" not in email and "." not in email:
    print(f"{email} je ve spatnem tvaru, chyby '@' nebo '.'")
    exit()
else:
    print(f"Email je v poradku")
print(oddelovac)

heslo = input("Zadej heslo: ")
if len(heslo) >= 8 and not heslo.isalpha() and not heslo.isnumeric():
    print("Heslo v poradku")
    print(oddelovac)
    # Poděkuj uživateli použitím jeho jména a informuuj jej/jí o provedení rezervace
    print(f"Dekuji: {jmeno} {prijmeni}")
    print(f"Zvolena destinace je: {ciloveMesto}")
    print(f"Cena je: {cena}")
    print(f"Jizdenku posleme na Vasi emailovou adresu: {email}")
else:
    print("""
    Tvoje heslo je spatne zadane:
    1. Musi obsahovat alespon 8 znaku,
    2. Musi obsahovat pismena,
    3. Musi obsahovat cislice
    """
    )