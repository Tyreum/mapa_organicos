from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import *
from accounts.serializer import ProdutorSerializer

import json

# Create your views here.

def accounts(request):
    return render(request, "accounts.html")


class Produtores(APIView):

    def get(self, *args, **kwargs):
        a = Produtor.objects.all()

        b = ProdutorSerializer(a, many=True)

        return Response(b.data)
