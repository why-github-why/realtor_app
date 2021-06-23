from django.contrib import messages  # from django.core.checks import messages
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from .models import Contact

def contact(request):
   if request.method == 'POST':
      listing_id = request.POST['listing_id']
      listing = request.POST['listing']
      name = request.POST['name']
      email = request.POST['email']
      phone = request.POST['phone']
      message = request.POST['message']
      user_id = request.POST['user_id']
      realtor_email = request.POST['realtor_email']

      # check if user made listing inquiry already
      if request.user.is_authenticated:
         user_id = request.user.id
         has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
         if has_contacted:
            messages.error(request, 'Inquiry already been made for this listing.')
            return redirect(f"/listings/{listing_id}")

      contact = Contact(
         listing_id=listing_id,
         listing=listing,
         name=name,
         email=email,
         phone=phone,
         message=message,
         user_id=user_id,
         )
      # save() - save to database
      contact.save()

      # email properties
      subject = f"{listing} - Property Listing Inquiry".upper()
      body = f"Property listing inquiry for {listing}. ❤️\n\nPlease sign in to admin area for more info."
      from_email = settings.EMAIL_HOST_USER  # 'smtplib2@gmail.com'
      recipient_list = [realtor_email, 'hello@leonkleinhans.com']
      # send email
      send_mail(subject=subject, message=body, from_email=from_email, recipient_list=recipient_list, fail_silently=False)

      # display message when inquiry request was successful
      messages.success(request, 'Request submitted. A realtor will get back to you soon.')

      return redirect(f"/listings/{listing_id}")  # return redirect('/listings/' + listing_id)
