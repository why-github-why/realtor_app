from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Post

def index(request):
   post_object = Post.objects.order_by('-subject_date').all()
   paginator = Paginator(post_object, 3)
   page = request.GET.get('page')
   page_posts = paginator.get_page(page)

   context = {
      'posts': page_posts,
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
