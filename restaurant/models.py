from django.db import models

class Restaurant(models.Model):
    name=models.CharField(max_length=100, unique=True)
    address=models.CharField(max_length=100)
    neighborhood=models.CharField(max_length=50, blank=True, null=True)
    cross=models.CharField(max_length=50, blank=True, null=True)
    lat=models.DecimalField(max_digits=10, decimal_places=7)
    lng=models.DecimalField(max_digits=10, decimal_places=7)
    phone=models.CharField(max_length=50, blank=True, null=True)
    reservations=models.CharField(max_length=50, blank=True, null=True)
    hours=models.CharField(max_length=50, blank=True, null=True)
    price=models.CharField(max_length=50, blank=True, null=True)
    cuisine=models.CharField(max_length=50, blank=True, null=True)
    subway_stop=models.CharField(max_length=50, blank=True, null=True)
    description=models.TextField(blank=True)
    last_visited_date=models.DateField()
    vote_yes=models.IntegerField()
    vote_no=models.IntegerField()

    def __unicode__(self):
        return self.name



class Comment(models.Model):
    restaurant=models.ForeignKey(Restaurant)
    #user=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    def __unicode__(self):
        return self.date



# Create your models here.
