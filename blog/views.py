from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    #print(allPosts)
    context = {'allPosts': allPosts} #badhi post ne blogHome templats ma mokele..context
    return render(request, 'blog/blogHome.html', context)
    #return HttpResponse('This is blogHome. we will keep all the blog posts here')

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first() #aa karvi atale first valu post j print thai
    post.views = post.views + 1
    post.save()
    
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:#video:96 min18 jovu kay nai karvu reply varamvarm print thai ena mate
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    #print(replyDict)

    #print(comments, replies)
    #print(request.user)
    context = {'post': post, 'comments': comments, 'user':request.user, 'replyDict':replyDict} #video 92
    return render(request, 'blog/blogPost.html', context)
    #return HttpResponse('This is blogPost: ') 


def postComment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)

            comment.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect(f"/blog/{post.slug}")
