from .models import User
from tweets.models import Tweet
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=Tweet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'tweets']