import requests

def menu_principal():
    print("\n === Convertisseur ===")
    print("1. Conversion de Température")
    print("2. Conversion de Longueur")
    print("3. Conversion de Poids")
    print("4. Conversion de Devises")
    print("5. Quitter")

def menu_temperature():
    print("\n Conversion de Température")
    print("1. Degrés → Kelvin")
    print("2. Kelvin → Degrés")
    print("3. Retour")

def menu_longueur():
    print("\n Conversion de Longueur")
    print("1. Mètres → Kilomètres")
    print("2. Kilomètres → Mètres")
    print("3. Retour")

def menu_poids():
    print("\n Conversion de Poids")
    print("1. Grammes → Kilogrammes")
    print("2. Kilogrammes → Grammes")
    print("3. Retour")

def menu_devises():
    print("\n Conversion de Devises")
    api_key = "73a15a97425e707ad2ceb2ca"
    url = "https://v6.exchangerate-api.com/v6/73a15a97425e707ad2ceb2ca/latest/USD"

    devise_depart = input("Devise de départ : ").upper()
    devise_cible = input("Devise cible : ").upper()
    montant = float(input("Montant à convertir : "))

    reponse = requests.get(url)
    if reponse.status_code == 200:
        data = reponse.json()
        taux = data['conversion_rates'].get(devise_cible)
        if taux:
            valeur_convertie = taux * montant
            print(f"\n{montant} {devise_depart} = {valeur_convertie:.2f} {devise_cible} (Taux: {taux})")
        else:
            print("Devise cible non trouvée.")
    else:
        print("Erreur lors de la récupération des données.")


while True:
    menu_principal()
    choix = input("Choisissez une option : ")

    if choix == "1":  
        while True:
            menu_temperature()
            temp_choix = input("Choix : ")
            if temp_choix == "1":
                valeur = float(input("Entrez la température en degrés : "))
                print(f"{valeur}° → {valeur + 273} K")
            elif temp_choix == "2":
                valeur = float(input("Entrez la température en Kelvin : "))
                print(f"{valeur} K → {valeur - 273}°")
            elif temp_choix == "3":
                break
            else:
                print(" Option invalide.")

    elif choix == "2":  
        while True:
            menu_longueur()
            long_choix = input("Choix : ")
            if long_choix == "1":
                valeur = float(input("Mètres : "))
                print(f"{valeur} m = {valeur * 0.001} km")
            elif long_choix == "2":
                valeur = float(input("Kilomètres : "))
                print(f"{valeur} km = {valeur * 1000} m")
            elif long_choix == "3":
                break
            else:
                print(" Option invalide.")

    elif choix == "3": 
        while True:
            menu_poids()
            poids_choix = input("Choix : ")
            if poids_choix == "1":
                valeur = float(input("Grammes : "))
                print(f"{valeur} g = {valeur * 0.001} kg")
            elif poids_choix == "2":
                valeur = float(input("Kilogrammes : "))
                print(f"{valeur} kg = {valeur * 1000} g")
            elif poids_choix == "3":
                break
            else:
                print(" Option invalide.")

    elif choix == "4":  
        menu_devises()

    elif choix == "5":  
        break

    else:
        print("Option invalide.")
