from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Post

def index(request):
   posts = Post.objects.order_by('-subject_date').all()

   context = {
      'posts': posts,
   }

   return render(request, 'blog/posts.html', context)  # 'blog/posts.html'

def post(request, post_id):
   # display 404 if object (page) doesn't exist
   # pk - private key
   post = get_object_or_404(Post, pk=post_id)

   context = {
      'post': post,
   }

   return render(request, 'blog/post.html', context)

def posts(request):
   all_posts = Post.objects.order_by('-subject_date').all()
   paginator = Paginator(all_posts, 3)  # 3
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)

   context = {
      'count': page_obj.count(),
      'posts': page_obj,
   }

   return render(request, 'blog.html', context)