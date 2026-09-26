# 1. Image de base : Python officiel version allégée
FROM python:3.11-slim

# 2. Dossier de travail dans le conteneur
WORKDIR /app

# 3. On copie D'ABORD requirements.txt (pour profiter du cache Docker)
COPY requirements.txt .

# 4. Installation des dépendances (--no-cache-dir = image plus légère)
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie le reste du code
COPY . .

# 6. On expose le port (le même que dans Uvicorn)
EXPOSE 8000

# 7. Commande de démarrage en production
CMD uvicorn 2_fatapi_Server_client:app --host 0.0.0.0 --port ${PORT:-8000}
