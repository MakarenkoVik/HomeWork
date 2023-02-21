from django.shortcuts import render
from store.models import Category, Game, Comment
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from datetime import date
from store.forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView


def index(request):
    order = request.GET.get("order_by")
    field, direction = "", ""
    games = Game.objects.filter(is_active = True)
    if order:
        field, direction = order.split(":")
        flow = "" if direction == "asc" else "-"
        if not field:
            field = "name"
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
    comments = game.comment_set.all().order_by('-pub_date')
    return render(request, "store/detail.html", {"game": game, "comments": comments})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    games = category.game_set.filter(is_active = True, category=category.id).all()
    return render(request, "store/category_detail.html", {"category": category, "games": games})


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.game = Game.objects.get(slug=self.kwargs["slug"])
        return super().form_valid(form)


class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy("store:index")
