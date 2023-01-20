from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,DeleteView, CreateView, UpdateView
from .models import post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

def hem(request):
    innehall = {'poster':Post.objects.all()}
    return render(request, 'blogg/hem.html',innehall)

class PostLista(ListView):
    model=post
    template_name = 'blogg/hem.html'
    context_object_name = 'poster'
    ordering = ['-datum_skapad']
    paginate_by= 2

class AnvamdarePostLista(ListView):
    model=post
    template_name = 'blogg/anvandare_poster.html'
    context_object_name = 'poster'
    ordering = ['-datum_skapad']
    paginate_by= 2

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(forfattare=user).order_by("-datum_skapad")

class PostSida(DetailView):
    model=post

class SkapaPost(LoginRequiredMixin, CreateView):
    model=post
    fields=['titel','innehall']
    
    def form_valid(self,form):
        form.instance.forfattare=self.request.user
        return super().form_valid(form)

class UppdateraPost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=post
    fields=['titel','innehall']
    
    def form_valid(self,form):
        form.instance.forfattare=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.forfattare:
            return True
        else:
            return False

class raderaPost(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=post
    success_url="/"

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.forfattare:
            return True
        else:
            return False

def om(request):
    return render(request, 'blogg/om.html',{'titel':'Om'})
