from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal received for user: {instance.username}")

try:
    with transaction.atomic():
        user = User.objects.create(username="testuser")
        print("User created, but rolling back...")
        raise Exception("Rolling back transaction")

except Exception as e:
    print(f"Transaction failed: {e}")

# Check if user exists
print("Users in DB:", User.objects.count())
