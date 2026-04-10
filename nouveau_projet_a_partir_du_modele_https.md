# Recommandations pour modifier le template dans un nouveau projet Github

A ajouter dans le projet "django-https-template"


Pour renommer correctement votre projet Django de **"htpps"** à **"blog"**, vous devez modifier plusieurs fichiers et configurations. Voici les étapes détaillées et les emplacements précis à vérifier :

---

### 1. **Renommer le dossier principal du projet**
- Le dossier principal de Django porte généralement le nom du projet (ici, `blog`).
- Renommez-le en `blog` :
  ```bash
  mv blog blog
  ```

---

### 2. **Modifier les fichiers de configuration Django**
#### a. **Fichier `manage.py`**
- Ouvrez `manage.py` et modifiez la ligne suivante :
  ```python
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
  ```
  en :
  ```python
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
  ```

#### b. **Fichier `blog/settings.py`**
- Ouvrez `blog/settings.py` (anciennement `blog/settings.py`).
- Modifiez les variables suivantes :
  ```python
  ROOT_URLCONF = 'blog.urls'  # → 'blog.urls'
  WSGI_APPLICATION = 'blog.wsgi.application'  # → 'blog.wsgi.application'
  ```

#### c. **Fichier `blog/urls.py`**
- Ouvrez `blog/urls.py` (anciennement `blog/urls.py`).
- Vérifiez que le nom du module est cohérent (pas de référence directe au nom du projet ici, sauf si vous avez des imports personnalisés).

---

### 3. **Renommer le fichier `wsgi.py` et `asgi.py` (si applicable)**
- Ouvrez `blog/wsgi.py` et vérifiez que la variable `application` est correcte :
  ```python
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
  ```

- Si vous utilisez ASGI (pour Django Channels), ouvrez `blog/asgi.py` et vérifiez :
  ```python
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
  ```

---

### 4. **Mettre à jour les références dans les fichiers de configuration du serveur (si HTTPS est configuré)**
- Si vous avez des fichiers de configuration pour le serveur web (par exemple, `nginx.conf` ou `apache.conf`), mettez à jour les chemins et les noms de projet pour refléter le nouveau nom (`blog` au lieu de `https`).

---

### 5. **Vérifier les imports personnalisés dans le code**
- Si vous avez des imports personnalisés dans vos applications ou vos fichiers Python qui font référence à `https`, mettez-les à jour pour utiliser `blog`.

---

### 6. **Nettoyer et tester**
- Supprimez les fichiers de cache Python :
  ```bash
  find . -type d -name "__pycache__" -exec rm -r {} +
  ```
- Testez votre projet :
  ```bash
  python manage.py runserver
  ```
- Vérifiez que tout fonctionne correctement et qu’aucune erreur ne persiste.

---

### 7. **Mettre à jour le dépôt Git (si nécessaire)**
- Si vous utilisez Git, assurez-vous de mettre à jour l’index et de commiter les changements :
  ```bash
  git add .
  git commit -m "Renommage du projet de blog à blog"
  git push origin main
  ```

---

### Résumé des fichiers modifiés
| Fichier/Emplacement          | Ancienne valeur          | Nouvelle valeur       |
|------------------------------|--------------------------|------------------------|
| `manage.py`                  | `https.settings`        | `blog.settings`        |
| `blog/settings.py`           | `https.urls`            | `blog.urls`            |
| `blog/settings.py`           | `https.wsgi.application`| `blog.wsgi.application`|
| `blog/wsgi.py`               | `https.settings`        | `blog.settings`        |
| (Optionnel) `blog/asgi.py`   | `https.settings`        | `blog.settings`        |

---

Si vous rencontrez des erreurs après ces modifications, vérifiez les traces d’erreur pour identifier les références manquantes ou incorrectes. Souhaitez-vous que je vous aide à vérifier un fichier spécifique ou à automatiser cette procédure ?
