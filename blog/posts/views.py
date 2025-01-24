from .models import Post
from django.shortcuts import redirect, render
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