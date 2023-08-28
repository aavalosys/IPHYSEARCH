
from django.db import models


class ArpCr(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ipcpe = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    vrf = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arp_cr'


class ArpGt(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ipcpe = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    vrf = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arp_gt'


class ArpHn(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ipcpe = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    vrf = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arp_hn'


class ArpNi(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ipcpe = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    vrf = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arp_ni'


class ArpPa(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ipcpe = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    vrf = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arp_pa'


class ArpSv(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ipcpe = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    vrf = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arp_sv'


class ArpXt(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ipcpe = models.CharField(max_length=32, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    vrf = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arp_xt'


class EquipoEquipos(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=False, primary_key=True)
    hostname = models.CharField(max_length=100, blank=True, null=True, )
    rol = models.CharField(max_length=10, blank=True, null=True)
    pais = models.CharField(max_length=10, blank=True, null=True)
    modelo = models.CharField(max_length=80, blank=True, null=True)
    version = models.CharField(max_length=80, blank=True, null=True)
    vendor = models.CharField(max_length=80, blank=True, null=True)
    localidad = models.CharField(max_length=800, blank=True, null=True)
    elabel = models.CharField(max_length=10000, blank=True, null=True)
    stp = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos'


class IntCr(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    ifindex = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    bw = models.CharField(max_length=40, blank=True, null=True)
    rx = models.CharField(max_length=40, blank=True, null=True)
    tx = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'int_cr'


class IntGt(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    ifindex = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    bw = models.CharField(max_length=40, blank=True, null=True)
    rx = models.CharField(max_length=40, blank=True, null=True)
    tx = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'int_gt'


class IntHn(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    ifindex = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    bw = models.CharField(max_length=40, blank=True, null=True)
    rx = models.CharField(max_length=40, blank=True, null=True)
    tx = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'int_hn'


class IntNi(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    ifindex = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    bw = models.CharField(max_length=40, blank=True, null=True)
    rx = models.CharField(max_length=40, blank=True, null=True)
    tx = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'int_ni'


class IntPa(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    ifindex = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    bw = models.CharField(max_length=40, blank=True, null=True)
    rx = models.CharField(max_length=40, blank=True, null=True)
    tx = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'int_pa'


class IntSv(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    ifindex = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    bw = models.CharField(max_length=40, blank=True, null=True)
    rx = models.CharField(max_length=40, blank=True, null=True)
    tx = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'int_sv'


class IntXt(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=30, blank=True, null=True)
    ifindex = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    bw = models.CharField(max_length=40, blank=True, null=True)
    rx = models.CharField(max_length=40, blank=True, null=True)
    tx = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'int_xt'


class MacAddressCr(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_address_cr'


class MacAddressGt(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_address_gt'


class MacAddressHn(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_address_hn'


class MacAddressNi(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_address_ni'


class MacAddressPa(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_address_pa'


class MacAddressSv(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_address_sv'


class MacAddressXt(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    mac = models.CharField(max_length=60, blank=True, null=True)
    vlan = models.CharField(max_length=30, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mac_address_xt'


class Nodob(models.Model):
    nodoid = models.CharField(max_length=16, blank=True, null=True)
    ip = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodob'


class Ospf(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    ospf_process = models.CharField(max_length=16, blank=True, null=True)
    router_id = models.CharField(max_length=16, blank=True, null=True)
    area = models.CharField(max_length=16, blank=True, null=True)
    interface = models.CharField(max_length=30, blank=True, null=True)
    neighbor = models.CharField(max_length=16, blank=True, null=True)
    estado = models.CharField(max_length=16, blank=True, null=True)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    costo = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ospf'


class PortChannel(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    logica = models.CharField(max_length=30, blank=True, null=True)
    fisica = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'port_channel'


class StaticHuaweivlan2G3Ggt(models.Model):
    ip = models.CharField(max_length=16, blank=True, null=True)
    iplo = models.CharField(max_length=16, blank=True, null=True)
    ipwan = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'static_huaweivlan2g3ggt'


class Vecinos(models.Model):
    hostname = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    interfaz = models.CharField(max_length=100, blank=True, null=True)
    hostnamev = models.CharField(max_length=100, blank=True, null=True)
    ipv = models.CharField(max_length=32, blank=True, null=True)
    interfazv = models.CharField(max_length=100, blank=True, null=True)
    protocolo = models.CharField(max_length=16, blank=True, null=True)
    pais = models.CharField(max_length=16, blank=True, null=True)
    paisv = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vecinos'
