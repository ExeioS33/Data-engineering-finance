# Utiliser une image Python officielle comme image parente
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt ./
COPY com_exeio_utils/ ./com_exeio_utils/
COPY create_tables.sql ./
COPY main.py ./
COPY wait-for-it.sh ./

# Rendre le script wait-for-it exécutable
RUN chmod +x wait-for-it.sh

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter le script en attendant que PostgreSQL soit prêt
CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "main.py"]
