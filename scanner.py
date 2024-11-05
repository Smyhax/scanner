import socket
import sys
from concurrent.futures import ThreadPoolExecutor # Pour le bonus multi-threading


def scan_port(target, port):
    """
    Cette fonction scanne un port spécifique sur une cible donnée

    Args:
        target (str): L'adresse IP de la cible
        port (int): Le numéro de port à scanner
    """
    try:
        # Création d'un socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Définition d'un timeout pour éviter les blocages trop longs
            s.settimeout(0.5) 
            # Tentative de connexion au por
            result = s.connect_ex((target, port))
            # Si la connexion réussit(code de retour 0), le port est ouvert
            if result == 0:
                print(f"--> Port {port}/TCP is open.")
    except KeyboardInterrupt:
        # Gestion de l'interruption par l'utilisateur (Ctrl+C)
        print("\nScan is stopping...")
        sys.exit(0)  # Arrêt propre du programme
    except Exception as e:
        pass  # Ignorer les autres erreurs (port probablement fermés)

def main():
    """
    Fonction principale du programme.
    """

    # Vérification du nombre d'arguments passés en ligne de commande
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target ip or hostname>")
        sys.exit(1)  # Arrêt avec un code d'erreur

    target = sys.argv[1]  # Récupération de la cible depuis les argument

    try:
        # Résolution du nom d'hôte en adresse IP
        target_ip = socket.gethostbyname(target)
        print(f"Scanning {target}...")

        # Utilisation de ThreadPoolExecutor pour le multi-threading
        with ThreadPoolExecutor(max_workers=100) as executor:
            try:
                for port in range(1, 1025):  # Scan des ports réservés (1-1024)
                    executor.submit(scan_port, target_ip, port)
                # Petit délai pour permettre au scan de se terminer proprement
                executor.shutdown(wait=True)
                print("Scan completed successfully.")
            except KeyboardInterrupt:
                print("CTRL + C")
                print("Scan is stopping...")
                executor.shutdown(wait=False)  # Arrêter proprement les threads restants
                print("\nScan completed successfully.")
                sys.exit(0)

    except socket.gaierror as error:
        # Gestion de l'erreur de resolution de nom d'hôte
        print(f"Hostname could not be resolved: {error}")
        sys.exit(1)  # Arrêt avec un code d'erreur pour l'utilisateur

# Exécution du programme principal seulement s'il est lancé directement
if __name__ == "__main__":
    main()