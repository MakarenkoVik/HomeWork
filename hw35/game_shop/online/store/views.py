from django.shortcuts import render
from store.models import Category, Game, Comment
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from store.forms import CommentForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.decorators import login_required
import datetime
import time
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from better_profanity import profanity
from store.tasks import replace_text_with_censored, info_log, info_log_db
from django.core import serializers


def index(request):
    log(request)
    log_db(request)
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


@cache_page(60 * 15)
def all_categories(request):
    log(request)
    log_db(request)
    categories = Category.objects.filter(is_active = True)
    return render(request, "store/categories.html", {"categories": categories})


def game(request: HttpRequest, slug):    
    log(request)
    log_db(request)
    cache_key = slug + "_game_cache"
    game = cache.get(cache_key)
    if not game:
        game = get_object_or_404(Game, is_active = True, slug=slug)
        cache.set(cache_key, game)    
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
    log(request)
    log_db(request)
    cache_key = slug + "_category_cache"
    category = cache.get(cache_key)
    if not category:
        category = get_object_or_404(Category, is_active = True, slug=slug)
        cache.set(cache_key, category)
    games = category.game_set.filter(is_active = True, category=category.id).all()
    return render(request, "store/category_detail.html", {"category": category, "games": games})


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse("store:game_detail", kwargs={"slug": self.object.game.slug})

    def form_valid(self, form):
        form.instance.game = Game.objects.get(slug=self.kwargs['slug'])
        self.object = form.save()
        replace_text_with_censored.delay(serializers.serialize('json', [self.object]))
        return HttpResponseRedirect(self.get_success_url())


class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy("store:index")


def log(request):
    path_log = str(request.path)
    user_log = str(request.user)
    time_log = datetime.datetime.now()
    info_log.delay(path_log, user_log, time_log)


def log_db(request):
    path_log = str(request.path)
    user_log = str(request.user)
    time_log = datetime.datetime.now()
    info_log_db.delay(path_log, user_log, time_log)
