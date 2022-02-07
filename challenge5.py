def verification(liste):
    local_liste = liste
    for officiel, pseudo in local_liste.items():
        indexx = 0
        for i in range(1, len(officiel)):
            if officiel[i].isupper() != False:
                indexx = i
                break
        verificateur = officiel[0:2].lower() + officiel[indexx : indexx + 2].lower()
        print(verificateur)
        if verificateur != pseudo:
            local_liste[officiel] = verificateur
    return local_liste

team = {"Farah Belhocine" : "fabe",
"Juliette Ustun" : "juus",
"Florian Torrente" : "flop",
"Dasha Chekeres" : "dach",
"Wiktor Ankurowski" : "wiak",
"Jeremy Zumstein" : "jesus",
"Ivan Dylevskiy" : "ivdy",
"Romain Campanale" : "roco",
"Youssef Chabouh" : "yoyo",
"Alexis Ramusat" : "alra"}
print(verification(team))