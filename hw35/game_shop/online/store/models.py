from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db.models import Avg
from django.contrib.auth.models import User



class ShopInfoMixin(models.Model):
    is_active = models.BooleanField(verbose_name="Is active?", default=True)
    slug =  models.SlugField(max_length=30, verbose_name="Slug")

    class Meta:
        abstract = True


class Category(ShopInfoMixin):
    title = models.CharField(max_length=50, verbose_name="Category Title")
    description = models.TextField(verbose_name="Category Description", blank=True, null=True)
    game_number = models.IntegerField(default=0, blank=True, null=True, verbose_name="Category games number")
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.title}"


def default_category():
    try:
        return Category.objects.get(title = "default").pk
    except:
        return None


class Game(ShopInfoMixin):
    name = models.CharField(max_length=50, verbose_name="Game name")
    pub_date = models.DateField(verbose_name="Game pub date", auto_now_add=True)
    release_date = models.DateField(verbose_name="Game release date")
    price = models.DecimalField(verbose_name="Game Price", max_length=4, max_digits=4, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=default_category, null=True, blank=True, verbose_name="Game Category")
    description = RichTextField(verbose_name="Game Description")
    game_image = models.ImageField(upload_to="game", blank=True, null=True, verbose_name="Game Image")

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"
        indexes = [
            models.Index(fields=["release_date"])
        ]
    
    def __str__(self):
        return f"{self.name}"
    
    def img_tag(self):
        return mark_safe(f'<img src = "{self.game_image.url}" width = "300"/>')

    def av_rating(self):
        result = self.comment_set.aggregate(Avg("rating"))
        if result['rating__avg'] == None:
            return "No rating"
        else:
            return f"Rating {result['rating__avg']:.2f} / 10"
        

class Comment(models.Model):
    text = models.CharField(max_length=100, verbose_name="Comment text")
    pub_date = models.DateField(verbose_name="Comment publication date", auto_now_add=True)
    rating = models.IntegerField(verbose_name="Comment rating")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Comment game")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, verbose_name="User's comment")

    def get_absolute_url(self):
        return reverse("store:game_detail", kwargs={"slug": self.game.slug})


class Log(models.Model):
    path = models.CharField(verbose_name="Url", blank=True, null=True, max_length=100)
    user_name = models.CharField(verbose_name="User", blank=True, null=True, max_length=100)
    date_time = models.DateTimeField(verbose_name="Date time", auto_now_add=True)
