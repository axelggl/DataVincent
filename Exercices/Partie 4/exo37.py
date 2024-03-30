import json
import os

# Fonction pour charger les tâches depuis un fichier JSON
def charger_taches():
    if os.path.exists("taches.json"):
        with open("taches.json", "r") as file:
            return json.load(file)
    else:
        return []

# Fonction pour sauvegarder les tâches dans un fichier JSON
def sauvegarder_taches(taches):
    with open("taches.json", "w") as file:
        json.dump(taches, file)

# Fonction pour afficher les tâches
def afficher_taches(taches):
    if taches:
        print("\nListe des tâches:\n")
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")
    else:
        print("\nAucune tâche à faire pour le moment.\n")

# Fonction pour ajouter une tâche
def ajouter_tache(taches, nouvelle_tache):
    taches.append(nouvelle_tache)
    sauvegarder_taches(taches)
    print("\nTâche ajoutée avec succès.\n")

# Fonction pour supprimer une tâche
def supprimer_tache(taches, numero_tache):
    if 1 <= numero_tache <= len(taches):
        tache_supprimee = taches.pop(numero_tache - 1)
        sauvegarder_taches(taches)
        print(f"Tâche '{tache_supprimee}' supprimée avec succès.")
    else:
        print("Numéro de tâche invalide.")

# Fonction principale
def main():
    taches = charger_taches()

    while True:
        print("\n\n\nBienvenue dans votre gestionnaire de tâches ! Que souhaitez-vous faire ?\n")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")

        choix = input("\nVotre choix : \n")

        # Remplacer ça par un switch case
        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            nouvelle_tache = input("Entrez la nouvelle tâche : ")
            ajouter_tache(taches, nouvelle_tache)
        elif choix == "3":
            afficher_taches(taches)
            numero_tache = int(input("Entrez le numéro de la tâche à supprimer : "))
            supprimer_tache(taches, numero_tache)
        elif choix == "4":
            print("\n\nMerci d'avoir utilisé le gestionnaire de tâches.\n\n")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
