### **🔨 Commandes Docker essentielles**

bash

```
# Construire l'image (-t = donner un tag/nom)
docker build -t mon-fastapi .

# Lancer un conteneur (-p = mapping port : hôte:conteneur)
docker run -p 8000:8000 mon-fastapi

# Lister les conteneurs en cours
docker ps

# Arrêter un conteneur
docker stop <id_du_conteneur>
```

Puis teste dans ton navigateur : `http://localhost:8000/hello` → tu dois voir `{"message":"bonjour"}` — **comme avant, mais maintenant c'est dans Docker**.
