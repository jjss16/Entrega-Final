from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .models import Serie, Comentario, Perfil
from .forms import SerieForm, ComentarioForm, UserRegistroForm, PerfilForm


def raiz(request):
    series = Serie.objects.all()
    return render(request, 'miapp/bienvenida.html', {'series': series})

@login_required
def crear_serie(request):
    if request.method == 'POST':
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raiz')
    else:
        form = SerieForm()

    return render(request, 'miapp/crear_serie.html', {'form': form})

@login_required
def ver_serie(request, pk):
    serie = get_object_or_404(Serie, pk=pk)
    comentarios = serie.comentarios.all()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.serie = serie
            comentario.usuario = request.user
            comentario.save()
            return redirect('ver_serie', pk=pk)
    else:
        comentario_form = ComentarioForm()

    return render(request, 'miapp/ver_serie.html', {'serie': serie, 'comentarios': comentarios, 'comentario_form': comentario_form})


def registrar_usuario(request):
    if request.method == 'POST':
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('raiz')
    else:
        form = UserRegistroForm()

    return render(request, 'miapp/registrar_usuario.html', {'form': form})

@login_required
def ver_perfil(request):
    perfil = request.user.perfil
    return render(request, 'miapp/ver_perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil = request.user.perfil
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('ver_perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'miapp/editar_perfil.html', {'form': form})