from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from blog.models import Post
from realtors.models import Realtor
from listings.choices import *

def index(request):
   # [:3] - Display only 3 listings
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
   posts = Post.objects.order_by('-subject_date').all()[:3]

   context = {
      'listings': listings,
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'posts': posts,
   }

   return render(request, 'pages/index.html', context)

def about(request):
   # Get all realtors
   realtors = Realtor.objects.order_by('hire_date')

   # Get MVP realtor(s)
   mvp_realtors = Realtor.objects.filter(is_mvp=True)
   
   context = {
      'realtors': realtors,
      'mvp_realtors': mvp_realtors,
   }

   return render(request, 'pages/about.html', context)
