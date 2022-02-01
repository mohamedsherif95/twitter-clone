from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name='tweets'


urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('tweets/', views.TweetsView.as_view(), name='get_tweets'),
    path('tweets/<int:pk>', views.TweetDetailsView.as_view(), name='get_tweet'),
    
    
    path('generic/tweets/', views.TweetsList.as_view()),
    path('generic/tweets/<int:pk>', views.TweetDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)