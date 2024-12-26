from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import descargar, busca_ips, busca_impactointerface, busca_impactoporpe, busca_varios,revisionftp, about, cgnatreport, actividades, casossr, descargar, varias_func, login, welcome, error

urlpatterns = [
    path('login/', login.login_view, name='login'),
    path('password-change/', login_required(auth_views.PasswordChangeView.as_view(template_name='password_change.html')), name='password_change',),
    path('password-change-done/',login_required(auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html')), name='password_change_done', ),
    path('welcome/', login_required(welcome.home), name='welcome'),    
    path('buscaips', login_required(busca_ips.buscaips), name='buscaips'), 
    path('detalleinterface/<str:dbcpe>/<str:ipsw>/<str:interface>/', varias_func.detalleinterface, name='detalleinterface'),
    path('pingdesdepevpn/<str:ippe>/<str:ipcpe>/<str:vrf>/', varias_func.pingdesdepevpn, name='pingdesdepevpn'), 
    path('impactointerfaces', busca_impactointerface.impactointerfaces, name='impactointerfaces'),
    path('buscasaturacion/<str:ip>/<str:no>/<str:dbinter>/<str:pais>/', busca_impactointerface.verimpactointerface, name='buscasaturacion'), 
    path('impactoporpe', busca_impactoporpe.impactoporpe, name='impactoporpe'),
    path('buscavarios/<str:selectedoption>/', busca_varios.buscavarios, name='buscavarios'), 
    path('buscar_macajax/<str:ippe>/<str:ipcpe>/<str:mac>/<str:vlan>/<str:interface>/<str:vrf>/<str:pais>/<str:dbcpe>/', busca_ips.buscaserviciomacajax, name='buscar_macajax'), 
    path('agregar_act/<int:pagina>/', login_required(actividades.actividades), name='agregar_act'),
    path('actualizacionactividades/<str:registroactividad>/', actividades.actualizacionactividades, name='actualizacionactividades'), #VER ACTUALIZACION ACTIVIDAD
    path('agregar_act/<int:pagina>/obtiene_vendors_estados/', actividades.obtiene_vendors_estados, name='obtiene_vendors_estados'),  
    path('agregar_act/actividades/<int:pagina>/actualizacionact/<str:registroact>/<str:fechaactmodal>/<str:actualizacion>/<str:usuarioact>/<str:estadoact>/<str:vendoract>/', actividades.actualizaractividad, name='actualizacionact'),    
    path('agregar_sr/<int:pagina>/', login_required(casossr.casossr), name='agregar_sr'),  
    path('agregar_sr/<int:pagina>/obtiene_proveedores_estados_paises/', casossr.obtiene_proveedores_estados_paises, name='obtiene_proveedores_estados_paises'),
    path('agregar_sr/casossr/<int:pagina>/actualizacionsr/<str:registrosr>/<str:fechahoragrabacion>/<str:rma>/<str:ttrma>/<str:fecharmain>/<str:actualizacion>/<str:usuariosr>/<str:estadosr>/<str:vendorsr>/<str:paissr>/', casossr.actualizarsrs, name='actualizacionsr'),
    path('agregar_sr/casossr/<int:pagina>/cierrermas/<str:registrosr>/<str:fechahoragrabacion>/<str:rmarecibido>/<str:ttrmarecibido>/<str:fecharmasrcierre>/<str:actualizacioncierre>/<str:usuariosr>/<str:estadosr>/<str:vendorsr>/<str:paissr>/', casossr.cierrermas, name='cierrermas'),
    path('muestradescripcionact/<str:registro>/', actividades.mostrarInformacionDescripcionact, name='muestradescripcionact'),
    path('muestradescripcionsr/<str:registro>/', casossr.mostrarInformacionDescripcionsr, name='muestradescripcionsr'), 
    path('revisionftp', login_required(revisionftp.revisionftpf), name='revisionftp'), 
    path('cgnatreport', login_required(cgnatreport.cgnat), name='cgnatreport'),
    path('descargarcsv/<str:pais>/', descargar.descargararchivo, name='descargarcsv'), 
    path('about', login_required(about.about), name='about'),
    path('logout/', login.logout_view, name='logout'),
    path('errorpage/', error.errorpage, name='errorpage'),
] 
