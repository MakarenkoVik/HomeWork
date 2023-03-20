from better_profanity import profanity
import time
from django.core import serializers
from celery import shared_task
from .models import Log
import datetime
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .models import Game, Comment
from django.contrib.auth.models import User
import datetime
from typing import List
from django.db.models import Avg


profanity.load_censor_words()

@shared_task()
def replace_text_with_censored(instance):
    instance = list(serializers.deserialize('json', instance))[0].object
    print("Before", instance.text)
    censored_text = profanity.censor(instance.text)
    time.sleep(5)
    instance.text = censored_text
    instance.save()
    print("After", instance.text)


@shared_task()
def info_log(path_log, user_log, time_log):
    message = f"{path_log} | {user_log} | {time_log}"
    print(message)


@shared_task()
def info_log_db(path_log, user_log, time_log):
    log = Log()
    log.user_name = user_log
    log.date_time = time_log
    log.path = path_log
    log.save(force_insert=True)


@shared_task()
def send_news_email_task(games: List[dict], top_games: list, user: dict):
    message_text = f'Hello {user["username"]}! See all our updates from last week!\n'
    for game in games:
        msg_chunk = f"""
        {games['name']} added at {games['release_date']}, price - {games['price']}.
        More details: { reverse_lazy("store:game_detail", kwargs={"slug": game.slug}) }
        """
        message_text += msg_chunk
    message_text += f'{user["username"]}, also see top three game!\n'
    for game_id in top_games:
        game = Game.objects.get(id=game_id)
        msg_top = f"""
        {game.name} has a rating {game.av_rating}.
        More details: { reverse_lazy("store:game_detail", kwargs={"slug": game.slug}) }
        """
        message_text += msg_top
    send_mail(
        "Weekly news", 
        message_text,
        "support@example.com",
        [user['email']],
        fail_silently=False,
    )


@shared_task()
def weekly_notification():
    all_users = list(User.objects.filter(is_staff=False).values())
    all_new_games = list(Game.objects.filter(pub_date__gte=datetime.datetime.today()-datetime.timedelta(days=7)).values())
    top_games = {}
    for game in Game.objects.all():
        top_games[game.id] = game.av_rating()
    if len(top_games) > 3:
        top_games = sorted(top_games)[:3]    
    for user in all_users:
        send_news_email_task.delay(all_new_games, top_games, user)
