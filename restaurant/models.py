from django.db import models
from django.forms import ModelForm

#Use ISO-3166-2 for countries
COUNTRIES=(('US','USA'),
    ('CA','Canada'),
    ('UK','United Kingdom'),)

#Use standard Postal Abbreviations for US, Canada
STATES=(('NJ','New Jersey'),
    ('NY','New York'),
    ('ON','Ontario'),
    ('QC','Quebec'),)


class Restaurant(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug=models.CharField(max_length=100, unique=True, editable=False)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=2, choices=STATES, blank=True)
    postcode=models.CharField(max_length=7, blank=True)
    country=models.CharField(max_length=2, choices=COUNTRIES)
    neighborhood=models.CharField(max_length=50, blank=True)
    cross=models.CharField(max_length=50, blank=True)
    lat=models.CharField(max_length=10,default='0', blank=True, editable=False)
    lng=models.CharField(max_length=10,default='0', blank=True, editable=False)
    phone=models.CharField(max_length=50, blank=True)
    reservations=models.CharField(max_length=50, blank=True)
    hours=models.CharField(max_length=50, blank=True)
    price=models.CharField(max_length=50, blank=True)
    cuisine=models.CharField(max_length=50, blank=True)
    subway_stop=models.CharField(max_length=50, blank=True)
    description=models.TextField(blank=True)
    last_visited_date=models.DateField(blank=True, null=True, editable=False)
    vote_yes=models.IntegerField(default=0, blank=True, editable=False)
    vote_no=models.IntegerField(default=0, blank=True, editable=False)
    rank_pct=models.CharField(max_length=10, default='0', editable=False)

    def __unicode__(self):
        return self.name



class Comment(models.Model):
    restaurant=models.ForeignKey(Restaurant)
    #user=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    def __unicode__(self):
        return self.date


class RestaurantForm(ModelForm):
    class Meta:
        model=Restaurant
