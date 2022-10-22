from ..models import Avanzo
from empresavinculada.models import EmpresaVinculada

def get_empresasvinculadas():
    vinculadas = Avanzo.objects.all()
    return vinculadas

def get_empresavinculada(mea_pk):
    vinculadas = Avanzo.objects.get(pk=mea_pk)
    return vinculadas


def update_empresavinculada(mea_pk, new_mea):
    vinculada = get_empresavinculada(mea_pk)
    vinculada.nombre = new_mea["nombre"]
    vinculada.razon_social = new_mea["razon_social"]
    vinculada.nit = new_mea["nit"]
    vinculada.direccion = new_mea["direccion"]
    vinculada.avanzo = Avanzo.objects.get(pk=new_mea["avanzo"]['pk'])
    vinculada.save()
    return vinculada

def create_empresavinculada(mea):
    vinculada = EmpresaVinculada(
        nombre=mea["nombre"],
        razon_social=mea["razon_social"],
        nit=mea["nit"],
        direccion = mea["direccion"],
        avanzo= Avanzo.objects.get(pk=mea["avanzo"]["pk"]),
    )
    vinculada.save()
    return vinculada

def delete_empresavinculada(mea_pk):
    vinculadas = get_empresavinculada(mea_pk)
    vinculadas.delete()