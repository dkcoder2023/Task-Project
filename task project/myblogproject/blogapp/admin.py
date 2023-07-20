from django.contrib import admin
from .models import Blog,Comment

class BlogAdmin(admin.ModelAdmin):
    model=Blog
    list_display=['title', 'content', 'author', 'created_at']
admin.site.register(Blog,BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    model=Comment
    list_display=['blog', 'name','email','body','created_at']
admin.site.register(Comment,CommentAdmin)
