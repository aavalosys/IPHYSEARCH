from datetime import timedelta, datetime
from django.utils.timezone import now, make_aware, is_naive
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout

class RedirectIfNotAuthenticated:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lista de rutas públicas (permitidas sin autenticación)
        allowed_urls = [
            reverse('login'),
            reverse('password_change'),
            reverse('password_change_done'),
        ]

        exclude_urls = [
            '/admin/',  # Django Admin
            '/static/',  # Archivos estáticos (si están en debug)
        ]

        # Verificar si el usuario está autenticado
        if request.user.is_authenticated:
            # Manejo de inactividad
            last_activity_str = request.session.get('last_activity')  # Obtener la última actividad como string
            if last_activity_str:
                last_activity = datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S.%f')  # Convertir a datetime
                if is_naive(last_activity):  # Hacer que sea consciente de la zona horaria si es necesario
                    last_activity = make_aware(last_activity)

                elapsed_time = now() - last_activity
                if elapsed_time > timedelta(minutes=30):  # Tiempo de inactividad permitido
                    logout(request)
                    return redirect('login')  # Redirige al login tras cerrar sesión

            # Actualizar la última actividad (almacenada como string)
            request.session['last_activity'] = now().strftime('%Y-%m-%d %H:%M:%S.%f')

        else:  # Usuario no autenticado
            if not any(request.path.startswith(url) for url in exclude_urls):
                if request.path not in allowed_urls:
                    return redirect('login')

        # Continuar el procesamiento normal si las verificaciones pasan
        response = self.get_response(request)
        return response
