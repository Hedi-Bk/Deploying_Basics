"""
============================================================
  ÉTAPE 3 : Serveur HTTP minimal avec FastAPI
============================================================
Objectif : comprendre ce qu'est un serveur, une route, une requête.

Ce fichier contient UN SEUL endpoint : GET /hello
============================================================
"""

# ------------------------------------------------------------
# 1. Import de FastAPI
# ------------------------------------------------------------
# FastAPI est une CLASSE. On va en créer une instance (= un objet).
from fastapi import FastAPI


# ------------------------------------------------------------
# 2. Création de l'application (le "serveur")
# ------------------------------------------------------------
# "app" est l'objet principal. C'est LUI qui va :
#   - contenir toutes les routes
#   - être donné à Uvicorn pour être exécuté
app = FastAPI(
    title="Mon premier serveur",           # nom affiché dans /docs
    description="Démo étape 3 - GET /hello", # description
    version="0.1.0",                        # version
)


print("=" * 60)
print("🟢 [SERVEUR] FastAPI initialisé")
print("=" * 60)


# ------------------------------------------------------------
# 3. Définition de la route GET /hello
# ------------------------------------------------------------
# Le décorateur @app.get("/hello") dit à FastAPI :
#   "Quand un client fait GET /hello, exécute la fonction juste en dessous."
#
# La fonction s'appelle "hello" (peu importe le nom, mais autant être clair).
@app.get("/hello")
def hello():
    """
    Cette fonction est appelée automatiquement quand un client
    fait une requête GET sur http://localhost:8000/hello

    Elle retourne un dictionnaire Python.
    FastAPI le convertit AUTOMATIQUEMENT en JSON.
    """
    print("📥 [SERVEUR] Requête reçue sur GET /hello")

    # FastAPI convertira ce dict en {"message": "bonjour"}
    reponse = {"message": "bonjour"}

    print(f"📤 [SERVEUR] Réponse envoyée : {reponse}")
    return reponse


# ------------------------------------------------------------
# 4. Démarrage du serveur (SEULEMENT si on lance ce fichier)
# ------------------------------------------------------------
# Le bloc "if __name__ == '__main__':" s'exécute UNIQUEMENT
# quand on lance "python main.py" directement.
# Il ne s'exécute PAS si le fichier est importé ailleurs.
if __name__ == "__main__":
    import uvicorn

    print("\n🚀 [SERVEUR] Démarrage sur http://localhost:8000")
    print("📖 [SERVEUR] Documentation auto : http://localhost:8000/docs")
    print("🛑 [SERVEUR] Pour arrêter : Ctrl + C dans ce terminal")
    print("=" * 60)
    print()

    # uvicorn.run() lance le serveur en boucle infinie.
    # Arguments :
    #   "main:app"  → cherche "app" dans le fichier "main.py"
    #   host        → "127.0.0.1" = seulement cette machine
    #   port        → 8000 (choisis-en un libre)
    #   reload      → redémarre auto quand tu modifies le code (dev)
    uvicorn.run(
        "2_fatapi_Server_client:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )