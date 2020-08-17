from django.contrib import admin
from .models import Post
from .models import morepost


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content', 'date_posted')


admin.site.register(Post, PostAdmin)


class morepostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content', 'date_posted')


admin.site.register(morepost, PostAdmin)
