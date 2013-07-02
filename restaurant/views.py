# Restaurant Selector v0.1
# https://github.com/njdevil/restaurant-selector
# ©2013 Modular Programming Systems Inc
# released as GPL 3


from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import slugify
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext
from django.contrib.auth.models import User
from fueled.restaurant.models import Restaurant, RestaurantForm, Comment, UserForm, GroupForm, ExtendedUser
from fueled.restaurant.forms import LoginForm
import re
import requests

def index(request):
    if request.get_full_path()=="/random/":
        data=Restaurant.objects.all().order_by('?').values().extra(select={'commentcount':'select count(restaurant_comment.id) from restaurant_comment where restaurant_comment.restaurant_id=restaurant_restaurant.id'},)
    else:
        data=Restaurant.objects.all().order_by('-rank_pct').values().extra(select={'commentcount':'select count(restaurant_comment.id) from restaurant_comment where restaurant_comment.restaurant_id=restaurant_restaurant.id'},)
    if request.POST:
        post=request.POST.copy()
        x=Restaurant.objects.filter(pk=post["id"]).values()
        if post["vote"]=="yes":
            new_vote_yes=float(x[0]["vote_yes"])+1
            old_vote_no=float(x[0]["vote_no"])
            new_rank_pct="%.4f" % (new_vote_yes/(new_vote_yes+old_vote_no))
            Restaurant.objects.filter(pk=post["id"]).update(vote_yes=new_vote_yes, rank_pct=new_rank_pct)
        if post["vote"]=="no":
            old_vote_yes=float(x[0]["vote_yes"])
            new_vote_no=float(x[0]["vote_no"])+1
            new_rank_pct="%.4f" % (old_vote_yes/(old_vote_yes+new_vote_no))
            Restaurant.objects.filter(pk=post["id"]).update(vote_no=new_vote_no, rank_pct=new_rank_pct)
    return render_to_response('index.html', {'data': data, 'test':request.get_full_path()}, RequestContext(request))


def show_restaurant(request,restaurant):
    _detail="xxx"
    data=Restaurant.objects.filter(slug=restaurant).values().extra(select={'commentcount':'select count(restaurant_comment.id) from restaurant_comment where restaurant_comment.restaurant_id=restaurant_restaurant.id'},)
    commentnameid=data[0]["id"]
    comments=Comment.objects.filter(restaurant__name=data[0]["name"])
#    content=request.POST.get('postcontent','')
#    content=re.sub("<a href=.*?</a>","",content)
#    content=re.sub("<\?","",content)

 #   if content:
 #       Comment.objects.create(restaurant_id=commentnameid, user_id=request.user.id, content=content).save()

    if request.POST:
        post=request.POST.copy()
        x=Restaurant.objects.filter(pk=post["id"]).values()
        if "comment" in post:
            content=post["content"]
            content=re.sub("<a href=.*?</a>","",content)
            content=re.sub("<\?","",content)
            if content:
                Comment.objects.create(restaurant_id=post["id"], user_id=request.user.id, content=content).save()
        if "vote" in post: 
            if post["vote"]=="yes":
                new_vote_yes=float(x[0]["vote_yes"])+1
                old_vote_no=float(x[0]["vote_no"])
                new_rank_pct="%.4f" % (new_vote_yes/(new_vote_yes+old_vote_no))
                Restaurant.objects.filter(pk=post["id"]).update(vote_yes=new_vote_yes, rank_pct=new_rank_pct)
            if post["vote"]=="no":
                old_vote_yes=float(x[0]["vote_yes"])
                new_vote_no=float(x[0]["vote_no"])+1
                new_rank_pct="%.4f" % (old_vote_yes/(old_vote_yes+new_vote_no))
                Restaurant.objects.filter(pk=post["id"]).update(vote_no=new_vote_no, rank_pct=new_rank_pct)

    return render_to_response('index.html', {'data': data, 'detail': _detail, 'comments': comments}, RequestContext(request))

##############################
#LOGIN/LOGOUT, Profile Section
##############################

@login_required
def user_profile(request,username):
    if request.user != username:
        HttpResponseRedirect('/')
    user2=ExtendedUser.objects.filter(username=username).values()
    return render_to_response('profile.html', {'user2': user2,}, RequestContext(request))


@csrf_protect
def userlogin(request):
    c={}
    c.update(csrf(request))
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/user/'+request.POST.get('username'))
        return render_to_response('addform.html', {'c': c, 'form': form}, RequestContext(request))
    else:
        form=LoginForm()

    return render_to_response('addform.html', {'c': c, 'form': form}, RequestContext(request))


def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


##############################
#Add records section
##############################

def add_restaurant(request):
    title="Add New Restaurant"
    if request.method=="POST":
        form=RestaurantForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            address=form.cleaned_data["address"]
            city=form.cleaned_data["city"]
            try:
                state=form.cleaned_data["state"]
            except:
                state=""
            country=form.cleaned_data["country"]
            full_address=address+"+"+city+"+"+state+"+"+country
            google=requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+full_address+'&sensor=false')
            if "partial_match" in google.json["results"][0]:
                error="Google can't find this address for Geocoding. Please check it and re-enter."
                form=RestaurantForm()
                return render_to_response('add.html', {'form': form, 'title': title, 'error': error})
            else:
                newrecord=form.save(commit=False)
                newrecord.slug=slugify(name)
                newrecord.lat="%.5f" % google.json["results"][0]["geometry"]["location"]["lat"]
                newrecord.lng="%.5f" % google.json["results"][0]["geometry"]["location"]["lng"]
                newrecord.save()
                return HttpResponseRedirect("/")
    else:
        form=RestaurantForm()
    return render_to_response('addform.html', {'form': form, 'title': title,}, RequestContext(request))


def add_user(request):
    title="Add New User"
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            #create user initially
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            #get user just created, to change password with HASH, SALT
            temp=User.objects.get(username__exact=username)         
            temp.set_password(password)
            temp.save()
            return HttpResponseRedirect('/')
    else:
        form=UserForm()
    return render_to_response('addform.html', {'form': form, 'title': title,}, RequestContext(request))

def add_group(request):
    title="Add New Group"
    if request.method=="POST":
        form=GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=GroupForm()
    return render_to_response('addform.html', {'form': form, 'title': title,}, RequestContext(request))

