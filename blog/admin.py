from django.contrib import admin
from blog.models import Post, Category, Comment, Contact, Newsletter
# Register your models here.

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Newsletter)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)