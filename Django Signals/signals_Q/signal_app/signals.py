import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import TestModel

@receiver(post_save, sender=TestModel)
def signal_handler(sender, instance, **kwargs):
    transaction.on_commit(lambda: handle_signal(instance))

def handle_signal(instance):
    print(f"Signal handler called for {instance}")
    
    # Check if the signal runs in the same thread
    current_thread = threading.current_thread().name
    print(f"Signal is running in thread: {current_thread}")
    
    # Check if signal runs in the same database transaction
    if transaction.get_connection().in_atomic_block:
        print("Signal is running within a database transaction.")
    else:
        print("Signal is running outside a database transaction.")