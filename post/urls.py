
from django.contrib import admin
from django.urls import path
from comment.views import homeFunction,allPostFunction,singlePost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeFunction,name="home"),
    path('allpost/',allPostFunction,name="allpost"),
    path('singlepost/<int:id>/',singlePost,name="singlepost"),
    # path('comment/',comment,name="comment"),



]
