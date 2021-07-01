from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='blog'),
   path('<int:post_id>', views.post, name='post'),
   path('blog/', views.posts, name='posts'),
]
