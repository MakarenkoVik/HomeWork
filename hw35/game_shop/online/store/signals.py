from django.db.models import signals
from django.dispatch import receiver
from .models import Game, Category


@receiver(signals.post_save, sender=Game)
def increase_game_number(sender, instance, created, **kwargs):
    if created:
        category = instance.category
        category.game_number += 1
        category.save()


@receiver(signals.post_delete, sender=Game)
def decrease_game_number(sender, instance, **kwargs):
    category = instance.category
    category.game_number -= 1
    category.save()
