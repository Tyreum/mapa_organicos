from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.accounts),
    path("api/v1/accounts/produtores", views.Produtores.as_view())
]
