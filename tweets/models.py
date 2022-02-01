from django.db import models
from accounts.models import User
from helpers.models import TrackingModel



class Tweet(TrackingModel):
    author = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(User, null=True, blank=True)
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"<ID: {self.id} - Author: {self.author}>"
    