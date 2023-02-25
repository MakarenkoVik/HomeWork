from django.shortcuts import render
from store.models import Category, Game, Comment
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from datetime import date
from store.forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.decorators import login_required
import datetime


def index(request):
    print(request.GET.get("redirect_to"))
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
    
    name_view_time = slug + "_time"
    name_view_counter = slug + "_counter"
    
    visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    last_visited = request.COOKIES[name_view_time] if name_view_time in request.COOKIES else None
    last_visited_times = int(request.COOKIES[name_view_counter] if name_view_counter in request.COOKIES else 0)

    response = render(request, "store/detail.html", 
                      {"game": game, 
                       "comments": comments,
                       "last_visited": last_visited,
                       "last_visited_times": last_visited_times})

    last_visited_times += 1

    response.set_cookie(name_view_time, visit_time, max_age=datetime.timedelta(days=20))
    response.set_cookie(name_view_counter, last_visited_times, max_age=datetime.timedelta(days=20))
    return response


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
