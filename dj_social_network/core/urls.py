from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
path('',login_page,name='login'),
path('signup/',SignupView.as_view(),name='signup'),
path('logout/',logout_user,name='logout'),
path('profile/',Profile.as_view() ,name='profile'),
path('account-settings/',AccountSettingsView.as_view(),name='account-settings'),
path('new_post/',CreatePost.as_view(),name='new_post'),
path('user/<str:username>/',FriendProfile.as_view() ,name='friend-profile'),
path('search/',SearchResults.as_view() ,name='search'),
path('follow/<int:id>',follow_user,name='follow-user'),
path('unfollow/<int:id>',unfollow_user ,name='unfollow-user'),
path('home/',HomePage.as_view() ,name='homepage'),



]
