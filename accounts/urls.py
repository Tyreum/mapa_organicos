from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.accounts),
    path("api/v1/accounts/produtores", views.Produtores.as_view()),

    path("register", views.RegisterView.as_view()),
    path("login", views.LoginView.as_view()),
    path("perfil/<id_user>", views.perfil)
]
