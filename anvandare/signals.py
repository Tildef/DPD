from .models import Profil
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def skapa_profil(sender,instance,created,**kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save,sender=User)
def spara_profil(sender,instance,**kwargs):
    instance.profil.save()
