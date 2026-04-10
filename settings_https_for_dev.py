# settings_https_for_dev.py
#
# Voici les settings https, cookies et sessions pour le développement
# -----------------------------------------------
#   Il faut donc en tenir cmpte pour l'intégrer
#  dans chaque nouveau projet de développement
# 

# Sécurité générale
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Paramètres HTTPS (pour runserver_plus)
SECURE_SSL_REDIRECT = False  # Désactivé car runserver_plus gère le HTTPS

# Cookies et sessions
SESSION_COOKIE_SECURE = True    # Cookies de session en HTTPS uniquement
CSRF_COOKIE_SECURE = True       # Cookies CSRF en HTTPS uniquement
SESSION_COOKIE_HTTPONLY = True  # Cookies de session inaccessibles via JavaScript
CSRF_COOKIE_HTTPONLY = True     # Cookies CSRF inaccessibles via JavaScript
SESSION_COOKIE_SAMESITE = 'Lax'  # Protection contre les attaques CSRF
CSRF_COOKIE_SAMESITE = 'Lax'    # Protection contre les attaques CSRF

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... autres middlewares ...
]

# Backend de session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Stockage en base de données
SESSION_COOKIE_DOMAIN = None  # Important pour le développement local
SESSION_SAVE_EVERY_REQUEST = True  # Sauvegarde la session à chaque requête