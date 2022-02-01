from pyexpat import model
from rest_framework import serializers
from accounts.serializers import UserSerializer

from tweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Tweet
        fields = '__all__'