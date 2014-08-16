from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Member(models.Model):
    user = models.ForeignKey(User, unique=True)
    interests = models.ManyToManyField(Tag, blank=True)
    
    def __unicode__(self):
        return unicode(self.user) + ' - Member'

@receiver(post_save, sender=User)
def create_member_for_user(sender, instance, created, **kwargs):
    if created:
        Member(user=instance).save()
