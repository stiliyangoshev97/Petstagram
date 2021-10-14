from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Profile

UserModel = get_user_model()

# We use post_save because the profile will be created
# after the user is created and saved
@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
