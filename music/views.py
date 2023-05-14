from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *

class HomePage(ListView):
    paginate_by = 4
    model = Music
    template_name = 'music/main.html'
    context_object_name = 'songs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category_selected'] = 0
        context['best'] = BestSong.objects.all()
        return context


def show_song(request, song_id):
    return HttpResponse(f"Отображение статьи с id = {song_id}")


class SongCategory(ListView):
    paginate_by = 4
    model = Music
    template_name = 'music/main.html'
    context_object_name = 'songs'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['songs'] = Music.objects.filter

def show_category(request, category_id):
    songs = Music.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    best = BestSong.objects.all()

    context = {
        'songs': songs,
        'categories': categories,
        'best': best,
    }

    return render(request, 'music/main.html', context=context)


def detailed(request, pk):
    song = Music.objects.get(pk=pk)
    categories = Category.objects.all()
    best = BestSong.objects.all()

    context = {
            'song': song,
            'categories': categories,
            'best': best,
    }

    return render(request, 'music/detailed.html', context=context)


# def homepage(request):
#     singers = Author.objects.all()
#     songs = Music.objects.all()
#
#     context = {
#         'songs': songs,
#         'singers': singers,
#     }
#
#     return render(request, 'music/main.html', context=context)
#


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'music/register.html'
    success_url = reverse_lazy('music:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('music:homepage')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'music/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('music:homepage')


def logout_user(request):
    logout(request)
    return redirect('music:homepage')







