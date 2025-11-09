from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import TaskForm

from .models import Task

@login_required(login_url="/login/")
def index(request):
    return render(request, 'tasks/index.html')

class TaskBaseView(LoginRequiredMixin, View):
    login_url = "/login/"

    model = Task
    success_url = reverse_lazy('tasks:all')
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskListView(TaskBaseView, ListView):
    context_object_name = 'tasks_list'

class TaskCreateView(TaskBaseView, CreateView):
    form_class = TaskForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(TaskBaseView, UpdateView):
    form_class = TaskForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDeleteView(TaskBaseView, DeleteView):
    pass