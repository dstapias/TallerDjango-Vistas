from django.shortcuts import render
from .logic import logic_measurements as ms
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        measurements_dto = ms.get_measurements()
        measurements = serializers.serialize('json', measurements_dto)
        return HttpResponse(measurements, 'application/json')
    if request.method == 'POST':
        measurement_dto = ms.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ms.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto])
        return HttpResponse(measurement, 'application/json')
    
    if request.method == 'PUT':
        measurement_dto = ms.update_measurement(pk, json.loads(request.body))
        variable = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(variable, 'application/json')
    
    if request.method == 'DELETE':
        measurement_dto = ms.delete_measurement(pk)
        variable = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(variable, 'application/json')
    
    
