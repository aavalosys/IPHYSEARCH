from django.shortcuts import redirect
from django.urls import reverse

class RedirectIfNotAuthenticated:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        allowed_urls = [
            reverse('login'),
            reverse('welcome'),
            reverse('buscaips'),
            reverse('impactointerfaces'),
            reverse('impactoporpe'),
            reverse('monitoreotcns'),
            reverse('cgnatreport'),
            reverse('about'),
            reverse('agregar_act'),
            reverse('agregar_sr'),
            reverse('actualizarmodales'),
            reverse('about'),
            reverse('buscavarios', kwargs={'selectedoption': 'default_option'}),
            reverse('buscavarios', kwargs={'selectedoption': 'mac'}),
            reverse('buscavarios', kwargs={'selectedoption': 'arp'}),
            reverse('buscavarios', kwargs={'selectedoption': 'equipos'}),
            reverse('buscavarios', kwargs={'selectedoption': 'descripciones'}),
            reverse('buscavarios', kwargs={'selectedoption': 'valoresopticos'}),
            reverse('catalogo', kwargs={'selectedoption': 'default_option'}),
            reverse('catalogo', kwargs={'selectedoption': 'actividades'}),
            reverse('catalogo', kwargs={'selectedoption': 'casossr'}),
            reverse('catalogo', kwargs={'selectedoption': 'buscaregistros'}),
        ]

        exclude_urls = [
            '/descargarcsv/',
            '/pingdesdepevpn/',
            '/detalleinterface/',
            '/buscasaturacion/',
            '/buscar_mac/',
            '/buscar_macajax/',
            '/actualizacionactividades/',
            '/catalogos/actividades/actualizacionact/',
			'/catalogos/casossr/actualizacionsr/',
        ]

        if not request.user.is_authenticated:
            if any(request.path.startswith(url) for url in exclude_urls):
                return self.get_response(request)

            if request.path not in allowed_urls:
                return redirect('login')

        response = self.get_response(request)
        return response
