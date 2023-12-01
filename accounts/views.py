from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import *
from accounts.serializer import ProdutorSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Produtor
from django.contrib.auth import login
from django.db import IntegrityError
import json

# Create your views here.

def accounts(request):
    return render(request, "accounts.html")


class Produtores(APIView):

    def get(self, *args, **kwargs):
        a = Produtor.objects.all()

        b = ProdutorSerializer(a, many=True)

        return Response(b.data)


class RegisterView(View):

    def get(self, *args, **kwargs):

        return render(self.request, 'register.html')

    def post(self, *args, **kwargs):
        # Retrieve data from the POST request
        username = self.request.POST['username']
        first_name = self.request.POST['first_name']
        last_name = self.request.POST['last_name']
        email = self.request.POST['email']
        password1 = self.request.POST['password1']
        password2 = self.request.POST['password2']
        nome_fantasia = self.request.POST['nome_fantasia']
        logradouro = self.request.POST['logradouro']
        numero = self.request.POST['numero']
        latitude = self.request.POST['latitude']
        longitude = self.request.POST['longitude']
        tipo_produtor = self.request.POST['tipo_produtor']

        # Validate passwords
        if password1 != password2:
            messages.error(self.request, 'Passwords do not match')
            return render(self.request, 'register.html', {'validation_messages': messages})

        # Create User
        try:
            user = User.objects.create_user(username=username, email=email, password=password1,
                                            first_name=first_name, last_name=last_name)
        except IntegrityError:
            messages.error(self.request, 'Username or email already exists')
            return render(self.request, 'register.html', {'validation_messages': messages})

        login(self.request, user)

        # Create Produtor
        produtor = Produtor.objects.create(
            user=user,
            nome_fantasia=nome_fantasia,
            logradouro=logradouro,
            numero=numero,
            latitude=latitude,
            longitude=longitude,
            tipo_produtor=tipo_produtor
        )

        return redirect('home')

