from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
   list_display = ('id', 'subject', 'subject_date', 'category', 'author')
   list_display_links = ('id', 'subject')
   list_filter = ('author', 'category')
   search_fields = ('subject', 'category')
   list_per_page = 25

admin.site.register(Blog, BlogAdmin)

