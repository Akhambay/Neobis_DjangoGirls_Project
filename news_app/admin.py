from django.contrib import admin
from .models import Post
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_tag', 'post_date')
    search_fields = ['title', 'body']


admin.site.register(Post, NewsAdmin)
