from django.contrib import admin
from . import models

admin.site.site_header = "Kokoev"

class ImageInline(admin.StackedInline):
    model = models.ImagesForBlog

class CommentInline(admin.StackedInline):
    model = models.CommentsForBlog

@admin.register(models.Blog)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ImageInline, CommentInline]