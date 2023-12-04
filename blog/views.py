from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    # first_post = Post.objects.first()
    # last_post = Post.objects.last()

    # specific_post = Post.objects.get(title="satu")
    # filtered_post = Post.objects.filter(title__contains="")

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})