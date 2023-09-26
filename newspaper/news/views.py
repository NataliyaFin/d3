from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime
from django.utils import timezone

class PostsList(ListView):
    model = Post # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html' # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts' # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id') # выводим в обратном порядке
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(timezone.now()) # добавим переменную текущей даты time_now
        return context
    
class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

def home(request):
    return render(request, 'home.html')
