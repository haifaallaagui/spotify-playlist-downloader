# 🎧 Spotify Playlist Scraper and YouTube Music Downloader

Ce projet Python automatise le processus d'extraction de chansons depuis une playlist Spotify, de recherche de leurs vidéos correspondantes sur YouTube, et de téléchargement de l'audio au format MP3.

---

## 🔧 Fonctionnalités

- **Scraping Spotify** : Récupération des titres et artistes depuis une playlist Spotify.
- **Recherche YouTube** : Recherche de vidéos YouTube correspondant à chaque chanson.
- **Téléchargement MP3** : Téléchargement de l'audio des vidéos YouTube en format MP3.

---

## 📋 Prérequis

- Python 3.8 ou supérieur
- Navigateur **Google Chrome**
- **ChromeDriver** : Doit être téléchargé et son chemin spécifié dans le script.

### 📦 Librairies Python nécessaires

```bash
pip install selenium pandas youtubesearchpython yt-dlp
⚙️ Installation de ChromeDriver
Télécharge la version correcte de ChromeDriver correspondant à ta version de Google Chrome depuis :

👉 https://sites.google.com/chromium.org/driver/

Place-le dans un répertoire connu et configure son chemin dans le script si besoin.

▶️ Utilisation
🎛️ Arguments en ligne de commande

Argument	Description
-u, --url	URL de la playlist Spotify à scraper
-o, --output	Chemin de sortie du fichier CSV contenant les titres et artistes extraits
📌 Exemple
bash
Copy
Edit
python script.py -u "https://open.spotify.com/playlist/your_playlist_url" -o "output.csv"
###🔍 Étapes détaillées
1. Scraping de la playlist Spotify
Le script utilise Selenium pour ouvrir l'URL de la playlist et faire défiler la page pour charger toutes les chansons.

Il extrait les titres et noms des artistes.

Les données sont sauvegardées dans un fichier .csv.

2. Recherche sur YouTube
Pour chaque chanson, le script utilise youtubesearchpython pour trouver la vidéo YouTube correspondante.

Il enregistre les URL des vidéos.

3. Téléchargement des fichiers MP3
Le script utilise yt-dlp pour télécharger l’audio de la meilleure qualité disponible.

Les fichiers MP3 sont enregistrés dans un dossier défini dans la fonction download() du script.

###📝 Remarques
Vérifie que la version de ChromeDriver est compatible avec celle de ton navigateur Chrome.

Assure-toi que le dossier de téléchargement spécifié existe avant d'exécuter le script.

Si la playlist est longue ou lente à charger, tu peux ajuster le temps de défilement (scroll) dans le script.

