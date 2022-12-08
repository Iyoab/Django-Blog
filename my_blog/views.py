from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import *
from django.urls import reverse_lazy
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
class MyBlogHome(DataMixin, ListView):
    model = MyBlog
    template_name: str = 'my_blog/index.html'
    context_object_name:str= 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "IK's Blog")
        context = dict(list(context.items())+list(c_def.items()))
        return context

    def get_queryset(self):
        return MyBlog.objects.filter(is_published=True)


class Show_post(DataMixin, DetailView):
    model = MyBlog
    template_name = 'my_blog/post.html'
    context_object_name: str = 'post'
    slug_url_kwarg: str = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = context['post'])
        context = dict(list(context.items())+list(c_def.items()))
        return context


def search(request):
    '''Performing search functions by upper bar '''
    return HttpResponse('Performing search on the site')


class Show_posts_by_category(DataMixin,ListView):
    model = MyBlog
    template_name = 'my_blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Category - ' + str(context['posts'][0].cat))
        context = dict(list(context.items())+list(c_def.items()))
        return context


    def get_queryset(self):
        return MyBlog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published = True)


def about(request):
    # следующие 4 строки кода это пагинация для функций представления
    contact_list = MyBlog.objects.all()
    paginator = Paginator(contact_list,1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_blog/about.html', {'page_obj':page_obj,'title':'About Blog'})


def contact(request):
    return render(request, 'my_blog/contact.html')


class Create_post(LoginRequiredMixin,DataMixin,CreateView):
    form_class = AddPost
    template_name: str = 'my_blog/add_post.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Create a post")
        context = dict(list(context.items())+list(c_def.items()))
        return context


def show_instructions(request):
    return render(request, 'my_blog/add_post.html')


def show_polls(request):
    return render(request, 'my_blog/add_post.html')


def authorizations(request):
    return render(request, 'my_blog/auth_form.html')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name: str = 'my_blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Registration form")
        context = dict(list(context.items())+list(c_def.items()))
        return context


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name: str = 'my_blog/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Login")
        context = dict(list(context.items())+list(c_def.items()))
        return context

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name: str = 'my_blog/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = "Login")
        context = dict(list(context.items())+list(c_def.items()))
        return context


def logout_user(request):
    logout(request)
    return redirect('login')