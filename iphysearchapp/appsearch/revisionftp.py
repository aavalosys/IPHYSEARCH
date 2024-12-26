import logging
from django.shortcuts import render
from django.db import connection
from iphysearchapp.databases import DATABASES
from iphysearchapp.var_env import *
from iphysearchapp.connect import *
from appsearch.varias_func import *
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required 
from appsearch.varias_func import *
from ftplib import FTP
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


PATHS = [
    "/Backups-CMTS-CENAM/GT_CMTS",
    "/Backups-CMTS-CENAM/HN_CMTS",
    "/Backups-CMTS-CENAM/NIC_CMTS",
    "/Backups-CMTS-CENAM/SV_CMTS"
]
archivos = []
FILE_EXTENSION = ".log"  # Extensión de archivo a buscar (e.g., ".log", ".doc")
MIN_SIZE = 0 #1  # Peso mínimo en bytes (e.g., 1 byte para evitar archivos vacíos)
MAX_SIZE = 10_000_000_000_000 #10_000_000  # Peso máximo en bytes (10 MB como ejemplo)

def grupo_requerido(grupos_permitidos, respuesta, errordes, errores):
    def decorator(view_func):
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name__in=grupos_permitidos).exists():
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'errorpage.html', {
                    'respuesta': respuesta,
                    'errordes': errordes,
                    'errores': errores
                })
        return _wrapped_view
    return decorator

@login_required
@grupo_requerido(
    grupos_permitidos=['superuser','adminusers'],
    respuesta="Acceso denegado",
    errordes="No tiene permisos para acceder a esta página.",
    errores=[]
)
def revisionftpf(request): 
    username = request.user.username
    ftp = connect_ftp(FTP_HOST, FTP_USER, FTP_PASS)
    archivos_por_path = []
    
    if ftp:
        archivos_por_path = check_logs(ftp, PATHS, FILE_EXTENSION, MIN_SIZE, MAX_SIZE)
        ftp.quit() 
    
    return render(request, 'paginas/revisionftp.html', {
            'dbs': esquemata_general(),
            'PATHS': PATHS,
            'archivos_por_path': archivos_por_path,
            'user': username,
    })

def check_logs(ftp, paths, file_extension, min_size, max_size):
    resultados = {}

    for path in paths:
        try:
            ftp.cwd(path)
            files = ftp.nlst() 
            target_files = [file for file in files if file.endswith(file_extension)]
            
            if not target_files:
                resultados[path] = [["SIN ARCHIVOS REVISAR", "", ""]]
                continue
            
            valid_files = []
            for file in target_files:
                size = ftp.size(file)
                if min_size <= size <= max_size:
                    valid_files.append([file, file_extension, f"{size} bytes"])
            
            resultados[path] = valid_files if valid_files else [["SIN ARCHIVOS VÁLIDOS", "", ""]]
        
        except Exception as e:
            resultados[path] = [[f"ERROR: {str(e)}", "", ""]]
    
    return resultados

def connect_ftp(host, user, password):
    try:
        ftp = FTP(host)
        ftp.login(user=user, passwd=password)
        print("Conexión exitosa al servidor FTP.")
        return ftp
    except Exception as e:
        print(f"Error al conectar al servidor FTP: {e}")
        return None


