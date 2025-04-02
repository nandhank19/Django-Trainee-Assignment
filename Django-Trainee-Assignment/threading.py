import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Check main thread
print(f"Main thread: {threading.current_thread().name}")

# Create user (Signal will be triggered)
User.objects.create(username="testuser")
