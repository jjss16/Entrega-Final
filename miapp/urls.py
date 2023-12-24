from django.urls import path
from .views import raiz, crear_serie, ver_serie, registrar_usuario, ver_perfil, editar_perfil
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', raiz, name='raiz'),
    path('crear-serie/', crear_serie, name='crear_serie'),
    path('ver-serie/<int:pk>/', ver_serie, name='ver_serie'),
    path('registrar-usuario/', registrar_usuario, name='registrar_usuario'),
    path('ver-perfil/', ver_perfil, name='ver_perfil'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
