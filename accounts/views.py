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
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm

import json

# Create your views here.

def accounts(request):
    return render(request, "accounts.html")


def perfil(request, id_user):

    if username := request.user:
        user_obj = User.objects.get(username=username)
        if user_obj.id == id_user:
            return render(request, 'perfil-private.html')
        else:
            return render(request, 'perfil-public.html')
    else:
        print(":C")

    





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
            return render(self.request, 'register.html')

        if password1 == '':
            messages.error(self.request, 'Passwords cannot be blank')
            return render(self.request, 'register.html')

        # Create User
        try:
            user = User.objects.create_user(username=username, email=email, password=password1,
                                            first_name=first_name, last_name=last_name)
        except IntegrityError as ex:
            messages.error(self.request, 'Username or email already exists')
            return render(self.request, 'register.html')
        except ValueError as ex:
            messages.error(self.request, ex)
            return render(self.request, 'register.html')

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

        return redirect('/')


class LoginView(View):

    def get(self, *args, **kwargs):

        return render(self.request, 'login.html')

    def post(self, *args, **kwargs):
        print(self.request.POST)
        form = AuthenticationForm(self.request, self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                messages.success(self.request, f'Welcome, {username}!')
                return redirect('/') 
            
        print(form.cleaned_data)
        messages.error(self.request, 'Invalid username or password.')
        return render(self.request, 'login.html')
