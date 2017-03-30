from django.db import models

# Create your models here.

class ShortenURL(models.Model):
    url = models.CharField(max_length=250,)

    def __str__(self):
        return str(self.url)
    # this return function is to show the added data as a list on web app
    # to show the primary key or primary id
    # return str(self.id)

    # for python2
    def __unicode__(self):
        return str(self.url)
