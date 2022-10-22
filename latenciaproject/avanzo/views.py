from django.shortcuts import render
from .logic import avanzo_logic as lg
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def avanzo_view(request):
    if request.method == 'GET':
        id = request.GET.get("id",None)
        if id:
            avanzo_dto = lg.get_Avanzo(id)
            avanzo = serializers.serialize('json',[avanzo_dto])
            return HttpResponse(avanzo, 'application/json')
        else:
            avanzos_dto = lg.get_Avanzos()
            avanzos = serializers.serialize('json', avanzos_dto)
            return HttpResponse(avanzos, 'application/json')

    if request.method == 'POST':
        avanzo_dto = lg.create_Avanzo(json.loads(request.body))
        avanzo = serializers.serialize('json',[avanzo_dto])
        return HttpResponse(avanzo, 'application/json')

@csrf_exempt
def avanzo_view(request, pk):
    if request.method == 'PUT':
        avanzo_dto = lg.update_Avanzo(pk, json.loads(request.body))
        avanzo = serializers.serialize('json', [avanzo_dto,])
        return HttpResponse (avanzo, 'application/json')

# Create your views here.
