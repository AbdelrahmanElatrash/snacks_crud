from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , TemplateView ,CreateView,DeleteView,DetailView ,UpdateView
from .models import Snack
# Create your views here.

class Home(TemplateView):
    template_name="home.html"


class SnackListView(ListView):
    template_name="snacks.html"
    model=Snack
    context_object_name='snacks'

class SnackDetailView(DetailView):
    template_name='detailview.html'
    model=Snack


class SnackCreateView(CreateView):
    
    template_name='create_snack.html'
    model=Snack
    fields= "__all__"


class SnackUpdateView(UpdateView):
    template_name='update_snack.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snacks')


class SnackDeleteView(DeleteView):
    template_name='delete_snack.html'
    model=Snack
    success_url=reverse_lazy('snacks')