from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Blog

def index(request):
   # pass postgresql database as object
   # sort by most recent first
   # paginator - create pagination
   blogs = Blog.objects.order_by('-subject_date').all()
   paginator = Paginator(blogs, 3)
   blog = request.GET.get('blog')
   blogs = paginator.get_page(blog)

   context = {
      'blogs': blogs,
   }

   return render(request, 'listings/listings.html', context)

def blog(request, blog_id):
   # display 404 if object (page) doesn't exist
   blog = get_object_or_404(Blog, pk=blog_id)

   context = {
      'blog': blog,
   }

   return render(request, 'blogs/blog.html', context)
