
import requests

SERVER_URL = "http://localhost:8080/draw"


def main():
    print("=== Tableau interactif ===")
    print("Formes disponibles : point, line, circle, rectangle, square")

    shape = input("Quelle forme veux-tu dessiner ? ").lower().strip()

    if shape == "point":
        x = int(input("Position x : "))
        y = int(input("Position y : "))
        data = {"shape": "point", "x": x, "y": y}

    elif shape == "line":
        x1 = int(input("Position x1 : "))
        y1 = int(input("Position y1 : "))
        x2 = int(input("Position x2 : "))
        y2 = int(input("Position y2 : "))
        data = {"shape": "line","x1": x1,"y1": y1,"x2": x2,"y2": y2}

    elif shape == "circle":
        x = int(input("Centre x : "))
        y = int(input("Centre y : "))
        radius = int(input("Rayon : "))
        data = {"shape": "circle","x": x,"y": y,"radius": radius}

    elif shape == "rectangle":
        x = int(input("Position x : "))
        y = int(input("Position y : "))
        width = int(input("Largeur : "))
        height = int(input("Hauteur : "))
        data = {"shape": "rectangle","x": x,"y": y,"width": width,"height": height}

    elif shape == "square":
        x = int(input("Position x : "))
        y = int(input("Position y : "))
        cote = int(input("Longueur du côté : "))
        data = {"shape": "square","x": x,"y": y,"cote": cote}

    else:
        print("Forme inconnue.")
        return

    # Saisie de la couleur RGB
    print("Choisis une couleur RGB (valeurs de 0 à 255).")
    red = int(input("Rouge : "))
    green = int(input("Vert : "))
    blue = int(input("Bleu : "))

    if not all(0 <= value <= 255 for value in (red, green, blue)):
        print("Erreur : chaque composante RGB doit être comprise entre 0 et 255.")
        return

    data["color"] = [red, green, blue]

    # Envoi de la requête HTTP POST
    try:
        response = requests.post(SERVER_URL, json=data, timeout=5)
        print("Code HTTP :", response.status_code)
        print("Réponse du serveur :", response.text)
        response.raise_for_status()

    except requests.RequestException as error:
        print("Impossible de contacter le serveur :", error)


if __name__ == "__main__":
    main()
