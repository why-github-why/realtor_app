from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Post

def index(request):
   posts = Post.objects.order_by('-subject_date').all()

   context = {
      'posts': posts,
   }

   return render(request, 'blog/posts.html', context)

def post(request, post_id):
   # display 404 if object (page) doesn't exist
   # pk - private key
   post = get_object_or_404(Post, pk=post_id)

   context = {
      'post': post,
   }

   return render(request, 'blog/post.html', context)