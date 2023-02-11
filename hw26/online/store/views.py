from django.shortcuts import render
from store.models import Category, Game
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from datetime import date

# Create your views here.

def index(request):
    order = request.GET.get("order_by")
    field, direction = "", ""
    games = Game.objects.filter(is_active = True)
    if order:
        field, direction = order.split(":")
        flow = "" if direction == "asc" else "-"
        sorting = f"{flow}{field}"
        games = games.order_by(sorting)
    paginator = Paginator(games, 4)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "store/index.html", context={"page_obj": page_obj, "field": field, "direction": direction})

def all_categories(request):
    categories = Category.objects.filter(is_active = True)
    return render(request, "store/categories.html", {"categories": categories})

def game(request: HttpRequest, slug):
    game = Game.objects.get(is_active = True, slug=slug)
    return render(request, "store/detail.html", {"game": game})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    games = category.game_set.filter(is_active = True, category=category.id).all()
    return render(request, "store/category_detail.html", {"category": category, "games": games})
