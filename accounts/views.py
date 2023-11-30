from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import *

import json

# Create your views here.

def accounts(request):
    return render(request, "accounts.html")


class Produtores(APIView):

    def get(self, *args, **kwargs):
        a = Produtor.objects.all()
        return Response(json.dumps({"a": f'{a}'}))
