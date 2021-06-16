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
   search_query = Listing.objects.order_by('-list_date')

   # Keyword
   if 'keywords' in request.GET:
      # request.GET[name attribute in html]
      keywords = request.GET['keywords']
      # check if keywords exist
      if keywords:
         # icontains - check if paragraph (description) contains the keyword
         search_query = search_query.filter(description__icontains=keywords)

   # City
   if 'city' in request.GET:
      city = request.GET['city']
      if city:
         # iexact - exact city but case-insensitive
         search_query = search_query.filter(city__iexact=city)

   # State
   if 'state' in request.GET:
      state = request.GET['state']
      if state:
         search_query = search_query.filter(state__iexact=state)

   # Bedrooms
   if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
         search_query = search_query.filter(bedrooms__iexact=bedrooms)  # bedrooms__lte

   # Max Price
   if 'price' in request.GET:
      price = request.GET['price']
      if price:
         # lte - less than or equal to (up to queried price)
         search_query = search_query.filter(price__lte=price)

   context = {
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'listings': search_query,
      'search_values': request.GET,  # get all values from GET request
   }

   return render(request, 'listings/search.html', context)