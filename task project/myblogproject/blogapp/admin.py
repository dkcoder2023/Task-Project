from django.contrib import admin
from blogapp.models import Blog,Comment

class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model=Blog
        list_display=['title', 'content', 'author', 'created_at']
admin.site.register(Blog,BlogAdmin)


class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model=Comment
        list_display=['blog', 'author','text','likes','created_at']
admin.site.register(Comment,CommentAdmin)