from __future__ import unicode_literals
from django.utils import timezone
from django.db.models import Model, CharField, ForeignKey, DateTimeField, \
    CASCADE


# Create your models here.
class Task(Model):
    description = CharField(max_length=512)
    created_at = DateTimeField(default=timezone.now, blank=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.description

    def as_json(self):
        return dict(
            description=self.description)

    class Meta:
        ordering = ('created_at',)


class Tag(Model):
    title = CharField(max_length=256)
    task = ForeignKey(Task, on_delete=CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    def as_json(self):
        return dict(
            title=self.title)
