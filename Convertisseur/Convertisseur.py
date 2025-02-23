import requests

print("Convertisseur")
print("1. Degres en celsus")
print("2. Celsus en degres")
print("3. Conversion Devise")

Choix = input("Choisir une option :")

if Choix =="1":
    valeur = float(input("Rentrez la température en degres :"))
    celsus = valeur + 273
    print(celsus)

elif Choix =="2" :
    valeur = float(input("Rentrez une température en Celsus :"))
    degres = valeur - 273
    print(degres)

elif Choix =="3":

    api_key = "73a15a97425e707ad2ceb2ca"


    url = "https://v6.exchangerate-api.com/v6/73a15a97425e707ad2ceb2ca/latest/USD"

    Devise_de_départ = input("Devise de départ : ").upper()
    Devise_arriver = input("Devise cible: ").upper()
    Montant = float(input("Montant à convertir : "))

    reponse = requests.get(url)

    if reponse.status_code == 200 : 
        data = reponse.json()
        taux = data['conversion_rates'][Devise_arriver]
        valeur = taux * Montant
        print(f"\n {Montant} {Devise_de_départ} = {valeur:.2f} {Devise_arriver} (Taux: {taux})")
    else:
        print("Erreur lors de la récupération des données.")

else :
    print("Option invalide")    