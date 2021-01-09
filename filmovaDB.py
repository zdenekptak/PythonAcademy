film1 = {
'JMENO': 'Shawshank Redemption',
'HODNOCENI': 93,
'ROK': 1994,
'REZISER': 'Frank Darabont',
'HRAJI': ['Tim Robbins', 'Morgan Freeman'],
'STOPAZ': "144 min"
}

film2 = {
'JMENO': 'The Godfather',
'HODNOCENI': 92,
'ROK': 1972,
'REZISER': 'Francis Ford Coppola',
'HRAJI': ['Al Pacino', 'Marlon Brando'],
'STOPAZ': "175 min"
}

film3 = {
'JMENO': 'The Dark Knight',
'HODNOCENI': 90,
'ROK': 2008,
'REZISER': 'Christopher Nolan',
'HRAJI': ['Christian Bale', 'Heath Ledger'],
'STOPAZ': "152 min"
}

ODDELOVAC = 100 * "="
filmy = [film1, film2, film3]
filmovaDB = dict()
for film in filmy:
    filmovaDB[film["JMENO"]] = film

filmyVDB = []

for f in filmovaDB.keys():
    filmyVDB.append(f)

print(ODDELOVAC)
print("Vitejte v nasi skromne filmove databazi")
print(ODDELOVAC)
print(f"Mame v nabidce tyto snimky: {filmyVDB}")
print(ODDELOVAC)
vybranyFilm = input("Vyberte film: ")
print(ODDELOVAC)
if vybranyFilm in filmyVDB:
    print(filmovaDB[vybranyFilm])
else:
    print("Zadali jste spatny nazev filmu")
