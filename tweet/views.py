from django.shortcuts import render
from .forms import TweetForm
from tweet.models import Post
from following.models import Userprofile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def homePage(request):
    form = TweetForm(request.POST or None)
    if request.user.is_authenticated!=True:
        return HttpResponseRedirect("/login")

    print("Logged in user : ",request.user)
    if request.method == 'POST':
        if form.is_valid():
            tweettitle=form.cleaned_data.get("title")
            tweettext=form.cleaned_data.get("text")
            tweet=form.save(commit=False)
            tweet.title = form.cleaned_data.get("title")
            tweet.text = form.cleaned_data.get("text")
            tweet.author = request.user
            tweet.save()
            form = TweetForm()

    followingUser= Userprofile.objects.get_or_create(user_name=request.user)[0].follows.all()
    curentUser =  User.objects.get(username=request.user)
    unfollowUserList = User.objects.all().difference(followingUser).order_by('-date_joined')
    tweetList = Post.objects.filter(author=request.user).filter(parent=None).order_by('-created_date')

    otherTweets = []
    for user_ in followingUser:
        otherTweets = Post.objects.filter(author=(user_))
        tweetList = tweetList | otherTweets
    tweetList = tweetList.order_by('-created_date')

    context={'tweet':form,'tweetList':tweetList,'usersList':unfollowUserList,'username':request.user}
    return render(request,"home.html",context)

@login_required
def tweetdetails(request,id):
    tweet = Post.objects.filter(id=(id))

    if tweet.exists() == False:
        print('in')
        return HttpResponseRedirect("/")

    child= Post.objects.filter(parent=(id))
    form = TweetForm(request.POST or None)
    if request.method == 'POST':
        print(request)
        if form.is_valid():
            tweettitle=form.cleaned_data.get("title")
            tweettext=form.cleaned_data.get("text")
            tweet1=form.save(commit=False)
            tweet1.title = form.cleaned_data.get("title")
            tweet1.text = form.cleaned_data.get("text")
            tweet1.author = request.user
            tweet1.author = request.user
            tweet1.parent = id
            tweet1.save()
            form = TweetForm()
    context={
    'tweet':tweet, 'form':form,'child':child
    }

    return render(request,"tweet.html",context)
