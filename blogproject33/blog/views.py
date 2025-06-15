from django.shortcuts import render, get_object_or_404
from .models import Post

# Show all posts
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # latest post first
    return render(request, 'home.html', {'posts': posts})

# Show individual post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


# Create your views here.
