from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from base.models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):
    model = Task

class TaskDetail(DetailView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields= '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields= '__all__'
    success_url= reverse_lazy('tasks')

class DeleteView (DeleteView):
    model= Task
    success_url = reverse_lazy('tasks')