from django.contrib import admin
from .models import Post

class BlogAdmin(admin.ModelAdmin):
   list_display = ('id', 'subject', 'category', 'subject_date', 'author')
   list_display_links = ('id', 'subject', 'author')
   list_filter = ('author', 'category')
   search_fields = ('subject', )
   list_per_page = 10

admin.site.register(Post, BlogAdmin)
