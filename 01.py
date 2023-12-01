
import forex_python
from forex_python.converter import CurrencyRates

monnaie = CurrencyRates()
historique = []
monnaiepref = []


while True:
    print("Voici vos monnaies préférées :",monnaiepref) 
    montant = int(input("Entrez le montant : "))
    a = input("Quelle devise utilisez-vous ? ")
    a1=input("Voulez vous ajouter cette devise dans vos préférées ?")
    if a1=="oui":
        monnaiepref.append(a)
    b = input("Vers quelle devise voulez-vous convertir ? ")
    

    print(a, "de", b, montant)

    resultat = monnaie.convert(a, b, montant)
    historique.append(resultat)

    print("Montant converti : ", resultat)
    
    c = input("Voulez-vous convertir une autre monnaie ? ")
    if c != "oui":
        break

d = input("Voulez-vous sauvegarder l'historique ? ")
if d == "oui":
    for i in historique:
        print(i)
