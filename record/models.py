from django.db import models
from django.db.models import CharField, URLField, IntegerField


class DramaRecord(models.Model):
    name = CharField(max_length=40)
    source = URLField()
    episode = IntegerField()
    max_episode = IntegerField()
    timestamp = CharField(max_length=8)

    def __str__(self):
        return "{}: {}/{} {}".format(self.name, self.episode, self.max_episode, self.timestamp)
