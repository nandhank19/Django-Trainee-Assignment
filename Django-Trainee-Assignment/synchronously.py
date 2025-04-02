import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal started...")
    time.sleep(5)  # Simulating a delay
    print("Signal finished!")

# Creating a user (Signal should block execution)
user = User.objects.create(username="testuser")
print("User creation completed.")
