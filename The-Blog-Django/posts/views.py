from django.shortcuts import render, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_http_methods
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.select_related('author').order_by('-pk')

    context = {
        'posts': posts
    }

    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.select_related('author'),
        pk = pk
    )

    context = {
        'post': post
    }

    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()

            return redirect('posts:post_detail', pk = post.pk)
    else:
        form = PostForm()
        
    context = {
        'form': form,
        'form_title': 'Crear Publicación'
    }

    return render(request, 'posts/post_form.html', context)

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if post.author_id != request.user.id:
        raise PermissionDenied

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)

        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', pk = post.pk)
    else:
        form = PostForm(instance = post)

    context = {
        'form': form,
        'form_title': 'Editar Publicación'
    }

    return render(request, 'posts/post_form.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def post_delete(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if post.author_id != request.user.id:
        raise PermissionDenied

    if request.method == 'POST':
        post.delete()
        return redirect('posts:post_list')

    context = {
        'post': post
    }

    return render(request, 'posts/post_confirm_delete.html', context)