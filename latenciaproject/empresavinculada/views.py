from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from .logic import empresasvinculadas_logic as ml

# Create your views here.

@csrf_exempt
def empresasvinculadas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id",None)
        if id:
            vinculada_dto = ml.get_empresavinculada(id)
            vinculada = serializers.serialize('json',[vinculada_dto])
            return  HttpResponse(vinculada,'application/json')
        else:
            vinculadas_dto = ml.get_empresasvinculadas()
            vinculadas = serializers.serialize('json',vinculadas_dto)
            return HttpResponse(vinculadas, 'application/json')

    if request.method == 'POST':
        vinculadas_dto = ml.create_empresavinculada(json.loads(request.body))
        vinculada = serializers.serialize('json',[vinculadas_dto])
        return HttpResponse(vinculada, 'application/json')

    if request.method == 'PUT':
        id = request.GET.get("id",None)
        vinculada_dto = ml.update_empresavinculada(id, json.loads(request.body))
        vinculada = serializers.serialize('json',[vinculada_dto])
        return HttpResponse(vinculada, 'application/json')

    if request.method == 'DELETE':
        id = request.GET.get("id", None)
        vinculada_dto = ml.delete_empresavinculada(id)
        return HttpResponse(vinculada_dto, 'application/json')

@csrf_exempt
def measurement_view(request, id):
    if request.method == 'GET':
        vinculada_dto = ml.get_empresavinculada(id)
        vinculada = serializers.serialize('json', [vinculada_dto])
        return HttpResponse(vinculada, 'application/json')

    if request.method == 'PUT':
        vinculada_dto = ml.update_empresavinculada(id, json.loads(request.body))
        vinculada = serializers.serialize('json',[vinculada_dto])
        return HttpResponse(vinculada, 'application/json')

    if request.method == 'DELETE':
        vinculada_dto = ml.delete_empresavinculada(id)
        return HttpResponse(vinculada_dto, 'application/json')