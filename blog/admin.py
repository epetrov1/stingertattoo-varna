from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

class BlogPostAdmin(SummernoteModelAdmin):  
    exclude = ('slug',)
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title','slug')
    summernote_fields = ('content',)

admin.site.register(BlogPost, BlogPostAdmin)