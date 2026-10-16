
import asyncio
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import websockets


# Clients connectés au tableau via WebSocket
connected_clients = set()

# Boucle asyncio utilisée par le serveur WebSocket
websocket_loop = None


# Gestion des requêtes HTTP
class DrawHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Vérifier l'URL demandée
        if self.path != "/draw":
            self.send_error(404, "Endpoint inconnu")
            return

        # Vérifier que le serveur WebSocket est prêt
        if websocket_loop is None:
            self.send_error(503, "Serveur WebSocket indisponible")
            return

        # Lire les données envoyées par le client
        try:
            content_length = int(self.headers.get("Content-Length", 0))

            if content_length <= 0:
                self.send_error(400, "Corps de requête vide")
                return

            body = self.rfile.read(content_length)
            data = json.loads(body.decode("utf-8"))

        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            self.send_error(400, "JSON invalide")
            return

        # Vérifier que les données reçues sont un objet JSON
        if not isinstance(data, dict):
            self.send_error(400, "Les données doivent être un objet JSON")
            return

        # Vérifier la présence du type de forme
        if data.get("shape") not in (
            "point", "line", "circle", "rectangle", "square"
        ):
            self.send_error(400, "Type de forme inconnu")
            return

        # Diffuser la forme aux tableaux connectés
        future = asyncio.run_coroutine_threadsafe(
            broadcast(data),
            websocket_loop
        )

        try:
            future.result(timeout=5)

        except Exception:
            self.send_error(500, "Erreur lors de la diffusion")
            return

        # Envoyer la réponse HTTP au client
        response = json.dumps({
            "status": "ok",
            "message": "Forme transmise"
        }).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    # Afficher les requêtes HTTP dans le terminal
    def log_message(self, format, *args):
        print(f"[HTTP] {args[0]}")


# Diffuser une forme à tous les tableaux connectés
async def broadcast(data):
    if not connected_clients:
        print("[WebSocket] Aucun tableau connecté.")
        return

    message = json.dumps(data)

    # Garder une liste stable pendant la diffusion
    clients = list(connected_clients)

    results = await asyncio.gather(
        *(client.send(message) for client in clients),
        return_exceptions=True
    )

    # Supprimer les connexions qui ne répondent plus
    for client, result in zip(clients, results):
        if isinstance(result, Exception):
            connected_clients.discard(client)


# Gérer les connexions WebSocket
async def websocket_handler(websocket):
    connected_clients.add(websocket)
    print("[WebSocket] Un tableau est connecté.")

    try:
        await websocket.wait_closed()
    finally:
        connected_clients.discard(websocket)
        print("[WebSocket] Un tableau s'est déconnecté.")


# Démarrer le serveur WebSocket
async def start_websocket_server():
    global websocket_loop

    websocket_loop = asyncio.get_running_loop()

    async with websockets.serve(
        websocket_handler,
        "localhost",
        8765
    ):
        print("[WebSocket] Serveur lancé sur le port 8765")
        await asyncio.Future()


# Démarrer le serveur HTTP dans un thread séparé
def start_http_server():
    server = ThreadingHTTPServer(
        ("localhost", 8080),
        DrawHandler
    )

    print("[HTTP] Serveur lancé sur le port 8080")

    try:
        server.serve_forever()
    finally:
        server.server_close()


# Lancer les deux serveurs
if __name__ == "__main__":
    http_thread = threading.Thread(
        target=start_http_server,
        daemon=True
    )
    http_thread.start()

    try:
        asyncio.run(start_websocket_server())
    except KeyboardInterrupt:
        print("\nArrêt des serveurs.")
