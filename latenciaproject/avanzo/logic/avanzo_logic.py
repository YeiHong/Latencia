from ..models import Avanzo

def get_Avanzos():
    avanzos = Avanzo.objects.all()
    return avanzos

def get_Avanzo(var_pk):
    avanzo = Avanzo.objects.get(pk=var_pk)
    return avanzo

def update_Avanzo(var_pk, new_var):
    avanzo = get_Avanzo(var_pk)
    avanzo.nombre = new_var["nombre"]
    avanzo.empresas_vinculadas = new_var[""]
    avanzo.save()
    return avanzo

def create_Avanzo(var):
    avanzo = Avanzo(nombre=var["nombre"])
    avanzo = Avanzo(empresas_vinculadas=var[""])
    avanzo.save()
    return avanzo