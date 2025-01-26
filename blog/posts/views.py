from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Post
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def post_list(request):
    post = Post.objects.all()
    return render(request, 'postlist.html', {'post1': post})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid:
            newpost = form.save(commit=False)
            newpost.created_by = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'post_new.html', { 'form': form })

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'details.html', {'post': post})

@login_required
def delete_post(request, post_id=None):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('posts:list')  
    return redirect('posts:list')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Отримуємо пост за ID

    if request.method == 'POST':
        form = forms.CreatePost(request.POST, instance=post)
        if form.is_valid():
            form.save()  # Зберігаємо оновлення
            return redirect('posts:list')  # Перенаправлення до деталей посту
    else:
        form = forms.CreatePost(instance=post)  # Заповнюємо форму існуючими даними

    return render(request, 'edit_post.html', {'form': form, 'post': post})