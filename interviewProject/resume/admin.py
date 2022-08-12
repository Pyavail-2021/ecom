from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=('title','content','url','added_date','image_tag')
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','content','category','created_date','url','image_tag')
    search_fields=('title',)
    list_filter=('title',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)