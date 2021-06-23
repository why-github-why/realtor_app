# when adding urls to app, urls must be added to project as well
# example: "path('contacts/', include('contacts.urls'))"

from django.urls import path
from . import views

urlpatterns = [
   path('contact', views.contact, name='contact'),
]
