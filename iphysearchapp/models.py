
from django.db import models



class Bitacora(models.Model):
    registrosractividad = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=45, blank=True, null=True)
    titulo = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.CharField(max_length=45, blank=True, null=True)
    hora = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    detalle = models.CharField(max_length=200, blank=True, null=True)
    observaciones = models.CharField(max_length=200, blank=True, null=True)
    vendor = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    pais = models.CharField(max_length=45, blank=True, null=True)
    tipo = models.CharField(max_length=45, blank=True, null=True)
    fechahoragrabacion = models.CharField(max_length=45, blank=True, null=True)
    usuariocrea = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitacora'
        app_label = 'iphysearchapp'


class Catalogos(models.Model):
    idcatalogo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    catalogotipo = models.CharField(max_length=45, blank=True, null=True)
    clasificador = models.CharField(max_length=45, blank=True, null=True)
    datoscatalogouno = models.CharField(max_length=45, blank=True, null=True)
    datoscatalogodos = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogos'
        app_label = 'iphysearchapp'


class Metadato(models.Model):
    idmetadato = models.BigIntegerField(primary_key=True)
    metadato_n = models.BigIntegerField(blank=True, null=True)
    metadato_s = models.CharField(max_length=45, blank=True, null=True)
    idoriginador = models.CharField(max_length=45, blank=True, null=True)
    fechahorain = models.CharField(max_length=45, blank=True, null=True)
    fechahoraout = models.CharField(max_length=45, blank=True, null=True)
    tipometadato = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metadato'
        app_label = 'iphysearchapp'


class Parametro(models.Model):
    idparametro = models.AutoField(primary_key=True)
    parametro = models.CharField(max_length=45, blank=True, null=True)
    codigo_propietario = models.CharField(db_column='codigo propietario', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    valor_nu = models.CharField(max_length=45, blank=True, null=True)
    valor_st = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    detalle = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parametro'
        app_label = 'iphysearchapp'


class Personas(models.Model):
    registrousuario = models.IntegerField(primary_key=True)
    codigousuario = models.CharField(max_length=45, blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    nombres = models.CharField(max_length=60, blank=True, null=True)
    apellidos = models.CharField(max_length=60, blank=True, null=True)
    token = models.CharField(max_length=45, blank=True, null=True)
    hashpassword = models.CharField(max_length=100, blank=True, null=True)
    rol = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    observaciones = models.CharField(max_length=100, blank=True, null=True)
    fechahoracreacion = models.CharField(max_length=45, blank=True, null=True)
    detalle = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    puesto = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=45, blank=True, null=True)
    idcatalogo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'
        app_label = 'iphysearchapp'


class Registrobitacora(models.Model):
    idregistro = models.AutoField(primary_key=True)
    fechafin = models.CharField(max_length=45, blank=True, null=True)
    horafin = models.CharField(max_length=45, blank=True, null=True)
    fechacierre = models.CharField(max_length=45, blank=True, null=True)
    horacierre = models.CharField(max_length=45, blank=True, null=True)
    fechahoragrabacion = models.CharField(max_length=45, blank=True, null=True)
    rma = models.CharField(max_length=90, blank=True, null=True)
    ttrma = models.CharField(max_length=90, blank=True, null=True)
    actualizacion = models.CharField(max_length=200, blank=True, null=True)
    detalle = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)
    usuariomodifica = models.CharField(max_length=45, blank=True, null=True)
    estadomodifica = models.CharField(max_length=45, blank=True, null=True)
    vendormodifica = models.CharField(max_length=50, blank=True, null=True)
    paismodifica = models.CharField(max_length=45, blank=True, null=True)
    clase = models.CharField(max_length=45, blank=True, null=True)
    bitacora_registrobitacora = models.ForeignKey(Bitacora, models.DO_NOTHING, db_column='bitacora_registrobitacora', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registrobitacora'
        app_label = 'iphysearchapp'


class Registroftp(models.Model):
    idregistroftp = models.IntegerField(primary_key=True)
    archivo = models.CharField(max_length=45, blank=True, null=True)
    peso = models.CharField(max_length=45, blank=True, null=True)
    fechahora = models.CharField(max_length=45, blank=True, null=True)
    ruta = models.CharField(max_length=45, blank=True, null=True)
    ftp = models.CharField(max_length=45, blank=True, null=True)
    plataforma = models.CharField(max_length=45, blank=True, null=True)
    ftpnumerico = models.CharField(max_length=45, blank=True, null=True)
    ftpstring = models.CharField(max_length=45, blank=True, null=True)
    idusuario = models.CharField(max_length=45, blank=True, null=True)
    fechahorausuario = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registroftp'
        app_label = 'iphysearchapp'


class Sesion(models.Model):
    registrosesion = models.AutoField(primary_key=True)
    fechagrabacion = models.CharField(max_length=45, blank=True, null=True)
    horagrabacion = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    tiempo = models.CharField(max_length=45, blank=True, null=True)
    timestamp = models.CharField(max_length=45, blank=True, null=True)
    datosesionuno = models.CharField(max_length=45, blank=True, null=True)
    codigousuario = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sesion'
        app_label = 'iphysearchapp'
