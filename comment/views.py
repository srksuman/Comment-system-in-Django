from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .forms import PostForm,CommentForm
from .models import Comment, Post
# Create your views here.
def homeFunction(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request,'html/home.html',{'form':form})

def allPostFunction(request):
    all_data = Post.objects.all()
    return render(request,'html/allPost.html',{'all_data':all_data})

def singlePost(request,id):
    data = Post.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        ids = request.POST.get('hidden')
        print("suman raj khanal")
        print(ids)
        if ids == "":
            if form.is_valid():
                name = form.cleaned_data['name']
                comments = form.cleaned_data['comments']
                dt = Comment(name=name,comments=comments,post = data)
                dt.save()
                return HttpResponseRedirect(f'/singlepost/{id}/')
        else:
            if form.is_valid():
                name = form.cleaned_data['name']
                comments = form.cleaned_data['comments']
                parent = Comment.objects.get(id=ids)
                dt = Comment(name=name,comments=comments,post = data,parent=parent)
                dt.save()
                return HttpResponseRedirect(f'/singlepost/{id}/')

    else:
        form = CommentForm()
        comment = Comment.objects.filter(post = data, parent=None)
        replies = Comment.objects.filter(post = data).exclude(parent=None)
        print('suman raj khanal')
        number = len(comment)
        print(replies)
    return render(request,'html/singlePost.html',{'data':data,'form':CommentForm,'comment':comment,'count':number,'reply':replies})

# def comment(request):
#     return HttpResponseRedirect('//')