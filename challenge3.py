def rendre_monnaie(article, prix, argentrecu):
    prix = float(prix)
    argentrecu = float(argentrecu)
    Monnaie_dispo = [100, 50, 20, 10, 5, 2, 1, 0.5]
    Monnaie_rendre = [0, 0, 0, 0, 0, 0, 0, 0]
    longueur = len(Monnaie_dispo)
    difference = argentrecu - prix
    
    for i in range(longueur):
        while difference >= Monnaie_dispo[i]:
            Monnaie_rendre[i] = Monnaie_rendre[i] + 1
            difference = difference - Monnaie_dispo[i]
    
    idk = []
    for i in range(longueur):
        if Monnaie_rendre[i] != 0:
            idk.append(f"{Monnaie_rendre[i]} x {Monnaie_dispo[i]}")
    
    Retour = [article] + idk
    return Retour


def function_caller(number):
    for i in range(number):
        article = input("article?")
        prix = input("prix ?")
        argent_donné = input("argent recu ?")
        print(rendre_monnaie(article, prix, argent_donné))
    return 0

commandes = int(input("nombre d'articles ?"))

function_caller(commandes)