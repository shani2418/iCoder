from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        #API to post a comment
    path('postComment', views.postComment, name="postComment"), #comment karvi atle pela rakhvu pade nakr blog vala nu jove

    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'), #slug lakhu atale views na blog ma vai jai
    

]
