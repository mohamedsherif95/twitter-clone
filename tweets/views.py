from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .permissions import IsAuthorOrReadOnly

def home_view(request):
    HOME_STR = '<h1>Hello World</h1>'
    return HttpResponse( HOME_STR)


class TweetsView(APIView, PageNumberPagination):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def get(self, request, format=None):
        queryset = Tweet.objects.all()
        tweets = self.paginate_queryset(queryset, request, view=self)
        serializer = TweetSerializer(tweets, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TweetDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# Generic APIs

class TweetsList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
