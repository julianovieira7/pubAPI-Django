import json

import requests
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Estabelecimento
from .serializers import EstabelecimentoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .util import APITOMTOM, KEYTOMTOM


class EstabelecimentoList(APIView):
    def get(self, request, latitude, longitude):
        latitude1 = float(latitude)
        longitude1 = float(longitude)
        try:
            lista_estabelecimentos = []
            if latitude is None or longitude is None:
                return JsonResponse({"mensagem": "latitude e longitude nâo podem ser nulo."}, status=status.HTTP_400_BAD_REQUEST)
            request = requests.get("{0}2/nearbySearch/.json?lat={1}&lon={2}&countrySet=BR%2C%20UTF-8&radius=5000&language=pt-BR&categorySet=9376003%2C%207315039&key={3}".format(APITOMTOM, latitude1, longitude1, KEYTOMTOM))
            todos = json.loads(request.content)
            for resultado in todos.get('results'):
                estabelecimento = Estabelecimento(resultado['poi']['name'], resultado['position']['lat'], resultado['position']['lon'])
                lista_estabelecimentos.append(estabelecimento)
            serializer = EstabelecimentoSerializer(lista_estabelecimentos, many=True)
            return Response(serializer.data)
        except Exception:
            return  JsonResponse({'mensagem': "Ocorreu um erro no servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)