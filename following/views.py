from django.shortcuts import render
from following.models import Userprofile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
@login_required
def followers(request):
    followingUser= Userprofile.objects.get_or_create(user_name=request.user)[0].follows.all()
    return render(request,"follower.html",{'usersList':followingUser})

@login_required
def followUnfollowUser(request,name):
    print('-------------')
    try:
        toFollow=User.objects.get(username=name)
        instance,created = Userprofile.objects.get_or_create(user_name=request.user)
        if instance.follows.all().filter(username=name).exists():
            instance.follows.remove(toFollow)  # Already following so unfollow
            print("Unfollowing ")
        else:
            print("New follow")
            instance.follows.add(toFollow)
    except:
        print('username doesnt exist')
        pass #Username doesnt exist
    return HttpResponseRedirect("/")
