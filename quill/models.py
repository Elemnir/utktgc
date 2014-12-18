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

class Thread(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Member, blank=True)
    sticky = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.creator.user) + " - " + self.title

    def last_updated(self):
        return self.post_set.latest('updated').updated

class Post(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Member, blank=True)
    thread = models.ForeignKey(Thread)
    body = models.TextField()

    def __unicode__(self):
        return u"{} - {} - {}".format(self.creator.user, 
            self.thread, self.title
        )

