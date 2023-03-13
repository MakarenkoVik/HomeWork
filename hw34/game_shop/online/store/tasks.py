from better_profanity import profanity
import time
from django.core import serializers
from celery import shared_task
from .models import Log
import datetime


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
