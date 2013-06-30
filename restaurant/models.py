from django.db import models

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
    slug=models.CharField(max_length=100, unique=True)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=2, choices=STATES, blank=True)
    postcode=models.CharField(max_length=7)
    country=models.CharField(max_length=2, choices=COUNTRIES)
    neighborhood=models.CharField(max_length=50, blank=True)
    cross=models.CharField(max_length=50, blank=True)
    lat=models.CharField(max_length=10,default='0', blank=True)
    lng=models.CharField(max_length=10,default='0', blank=True)
    phone=models.CharField(max_length=50, blank=True)
    reservations=models.CharField(max_length=50, blank=True)
    hours=models.CharField(max_length=50, blank=True)
    price=models.CharField(max_length=50, blank=True)
    cuisine=models.CharField(max_length=50, blank=True)
    subway_stop=models.CharField(max_length=50, blank=True)
    description=models.TextField(blank=True)
    last_visited_date=models.DateField(blank=True, null=True)
    vote_yes=models.IntegerField(blank=True)
    vote_no=models.IntegerField(blank=True)
    rank_pct=models.CharField(max_length=10, default='0')

    def __unicode__(self):
        return self.name



class Comment(models.Model):
    restaurant=models.ForeignKey(Restaurant)
    #user=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    def __unicode__(self):
        return self.date
