from django.contrib import admin

# Register your models here.

from store.models import Category, Game

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
