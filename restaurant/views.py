from django.shortcuts import render_to_response
from fueled.restaurant.models import Restaurant, Comment
import re

def index(request):
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
    return render_to_response('index.html', {'data': data})

def add_restaurant(request):
    pass

def edit_restaurant(request):
    pass

def show_restaurant(request,restaurant):
    _detail="x"
    data=Restaurant.objects.filter(slug=restaurant).values().extra(select={'commentcount':'select count(restaurant_comment.id) from restaurant_comment where restaurant_comment.restaurant_id=restaurant_restaurant.id'},)
    commentnameid=data[0]["id"]
    comments=Comment.objects.filter(restaurant__name=data[0]["name"])
    content=request.POST.get('postcontent','')
    content=re.sub("<a href=.*?</a>","",content)
    content=re.sub("<\?","",content)

    if content:
        Comment.objects.create(restaurant_id=commentnameid, content=content).save()

    return render_to_response('index.html', {'data': data, 'detail': _detail, 'comments': comments})
