from django.shortcuts import render
# from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Listing

def index(request):
   # pass postgresql database as object
   # sort by most recent first
   listings = Listing.objects.order_by('-list_date').filter(is_published=True)  # .all()
   paginator = Paginator(listings, 3)  # 6
   page = request.GET.get('page')
   page_listings = paginator.get_page(page)

   context = {
      'listings': page_listings,
   }

   return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
   return render(request, 'listings/listing.html')

def search(request):
   return render(request, 'listings/search.html')