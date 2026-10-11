from django.shortcuts import render, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
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
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()

            return redirect('posts:post_detail', pk = post.pk)
    else:
        form = PostForm()
        
    context = {
        'form': form
    }

    return render(request, 'posts/post_form.html', context)