from contacts.models import Contact
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
   if request.method == 'POST':

      # retrieve user input values (POST['..'] - refer to HTML input name='..')
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      confirm_password = request.POST['confirm_password']      

      # check if passwords match
      if password == confirm_password:

         # check if username already exists in db
         if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
         else:
            # check if email already exists in db
            if User.objects.filter(email=email).exists():
               messages.error(request, 'Email is already being used.')
               return redirect('register')
            else:
               # create user
               user = User.objects.create_user(
                  first_name = first_name,
                  last_name = last_name,
                  username = username,
                  email = email,
                  password = password,
               )
               user.save()
               messages.success(request, 'You are now registered.')
               return redirect('login')

      else:
         messages.error(request, 'Passwords does not match.')
         return redirect('register')

   else:
      return render(request, 'accounts/register.html')

def login(request):
   if request.method == 'POST':
      # login user
      username = request.POST['username']
      password = request.POST['password']

      # authenticate user
      user = auth.authenticate(username=username, password=password)

      # check if user exists in database
      if user is not None:
         auth.login(request, user)
         messages.success(request, 'You are now logged in.')
         return redirect('dashboard')
      else:
         messages.error(request, 'Invalid credentials.')
         return redirect('login')

   else:
      return render(request, 'accounts/login.html')

def logout(request):
   if request.method == 'POST':
      # logout user
      auth.logout(request)
      messages.success(request, 'You are now logged out.')
      return redirect('index')

def dashboard(request):
   # -contact_date - order by most recent first
   # user_id=request.user.id - get user id from current logged in user
   user_contacts = Contact.objects.order_by('-inquiry_date').filter(user_id=request.user.id)

   context = {
      'contacts': user_contacts,
   }

   return render(request, 'accounts/dashboard.html', context)
