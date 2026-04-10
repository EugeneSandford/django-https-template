# views.py
from django.http import HttpResponse

def check_https(request):
    return HttpResponse(f"HTTPS: {request.is_secure()}")

def check_session(request):
    if hasattr(request, 'session'):
        request.session['test_key'] = 'test_value'  # Définit une valeur de session
        return HttpResponse(f"Session ID: {request.session.session_key}, Test value: {request.session.get('test_key')}")
    else:
        return HttpResponse("No session found")


def home(request):
    if not request.session.session_key:  # Vérifie si la session existe
        request.session.create()          # Force la création de la session
    request.session['visited'] = True    # Stocke une valeur dans la session
    return HttpResponse("Session initialisée")