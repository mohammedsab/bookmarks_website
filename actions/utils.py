import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Action


def create_action(user, verb, target=None):
    # Check for any similer action in the last minute
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similer_actions = Action.objects.filter(
        user_id=user.id, verb=verb, created__gte=last_minute)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similer_actions = similer_actions.filter(
            target_ct=target_ct, target_id=target.id)
        
    if not similer_actions:
        # No existing actions found
        action = Action(user=user, verb=verb, target=target)
        action.save()

        return True
    return False
