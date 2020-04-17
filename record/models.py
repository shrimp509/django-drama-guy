from django.db import models
from django.db.models import CharField, URLField, TimeField, IntegerField


class DramaRecord(models.Model):
    name = CharField()
    source = URLField()
    episode = IntegerField()
    max_episode = IntegerField()
    timestamp = TimeField()

    def __str__(self):
        return "{}: {}/{} {}".format(self.name, self.episode, self.max_episode, self.timestamp)
