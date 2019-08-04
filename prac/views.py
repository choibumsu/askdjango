from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

# Create your views here.

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) #인자 순서 바뀌면 안됨
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/prac/')
    else:
        form = PostForm()
    return render(request, 'prac/post_form.html', {'form':form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) #인자 순서 바뀌면 안됨
        if form.is_valid():
            post = form.save(commit=False)
            post.id = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/prac/')
    else:
        form = PostForm(instance=post)
    return render(request, 'prac/post_form.html', {'form':form})