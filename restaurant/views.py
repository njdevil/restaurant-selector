from django.shortcuts import render_to_response
from fueled.restaurant.models import Restaurant, Comment

def index(request):
    pass

def add_restaurant(request):
    pass

def edit_restaurant(request):
    pass

def show_restaurant(request):
    data=Restaurant.objects.all()
    return render_to_response('index.html', {'data': data})
# Create your views here.
