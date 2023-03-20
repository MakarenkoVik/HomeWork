from django.contrib import admin
from store.models import Category, Game, Comment, Log
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.core import serializers
from django.http import FileResponse
from datetime import datetime
from django.db.models import Avg
import io

class GameInline(admin.StackedInline):
    model = Game

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("date_time", "user_name","path")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("game", "rating","text", "pub_date")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = (
        "title", 
        "view_game_link", 
        "average_price"
        )
    inlines = [
        GameInline,
    ]

    @admin.display(description="average price")
    def average_price(self, obj):
        result = Game.objects.filter(category=obj).aggregate(Avg("price"))
        return f'${result["price__avg"]:.2f}'

    @admin.display(description="games")
    def view_game_link(self, obj):
        count = obj.game_set.count()
        url = (
            reverse("admin:store_game_changelist")
            + "?"
            + urlencode({"category_id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Games</a>', url, count)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    date_hierarchy = "release_date"
    list_display = (
        "name", 
        "release_date",
        "show_price",
        "img_preview",
        "get_link"
    )
    list_editable = ("release_date",)
    list_filter = ("category",)
    search_fields = ("name", "category__title")
    readonly_fields = ("img_tag",)
    actions = ("make_inactive", "export_as_csv")

    @admin.display(description="custom price")
    def show_price(self, obj):
        return f"$ {obj.price}"

    @admin.display(description="game image")
    def img_preview(self, obj):
        return mark_safe(
            f'<img src = "{obj.game_image.url}" width ="150px" height="200px"/>'
        )
    
    @admin.display(description="game image")
    def img_tag(self, obj): 
        return mark_safe(
            f'<img src = "{obj.game_image.url}" width = "150" height="200px"/>'
        )

    @admin.display(description='game link')
    def get_link(self, obj):
        return mark_safe(
            f'<a href="https://ru.wikipedia.org/wiki/{obj.name}">Search</a>'
        )
    
    @admin.action(description = "Перевести в неактивное состояние")
    def make_inactive(self, request, queryset): 
        queryset.update(is_active=False)

    @admin.action(description="Download files")
    def export_as_csv(self, request, queryset):
        response = FileResponse(
            io.BytesIO(serializers.serialize("json", queryset).encode("utf-8")), 
            as_attachment=True, filename=f"log-{datetime.now()}.csv",
        )
        return response
