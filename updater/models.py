import hashlib
from datetime import datetime
from random import randint

from django.db import models
from django.contrib.auth.models import User

class Host(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    access_key = models.CharField(max_length=255, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.access_key:
            md5 = hashlib.md5()
            md5.update(str(datetime.now()))
            md5.update(self.name)
            self.access_key = md5.hexdigest()
        super(Host, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
            

class Update(models.Model):
    host = models.ForeignKey(Host)
    from_ip = models.CharField(max_length=255) # Is there such thing as an "IP-Field"? Maybe write one?
    message = models.TextField(blank=True) # optional TextMessage, a client can provide
    added = models.DateTimeField(auto_now_add=True)
    in_zone = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.host.name
