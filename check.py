# Fichier de vérification de l'environnement Python
# Projet : L'Atelier Énervant de Mathilde Martine PAISLEY
# Localisation : /Volumes/Partition MacOS_MPPA/Atelier_Enervant_Sandbox/check.py

import sys
import datetime

def verifier_systeme():
    print("\n--- 🧁 L'Atelier Énervant de Mathilde - Check Système ---")
    
    # Vérification de la version de Python 3
    version = sys.version.split()[0]
    print(f"✅ Version de Python détectée : {version}")
    
    # Vérification de la date et l'heure
    maintenant = datetime.datetime.now()
    print(f"✅ Date du test : {maintenant.strftime('%d/%m/%Y à %H:%M:%S')}")
    
    print("\n[INFO PM] : L'infrastructure est prête.")
    print("---------------------------------------------------------\n")

if __name__ == "__main__":
    verifier_systeme()
# Fichier de vérification de l'environnement Python
# Projet : L'Atelier Énervant de Mathilde Martine PAISLEY
# Localisation : /Volumes/Partition MacOS_MPPA/Atelier_Enervant_Sandbox/check.py