from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Listing
from .choices import *

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
   # display 404 if object (page) doesn't exist
   listing = get_object_or_404(Listing, pk=listing_id)

   context = {
      'listing': listing,
   }

   return render(request, 'listings/listing.html', context)

def search(request):
   context = {
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
   }

   return render(request, 'listings/search.html', context)