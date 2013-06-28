from models import Restaurant, Comment
from django.contrib import admin

class RestaurantAdmin(admin.ModelAdmin):
	#prepopulated_fields={"slug":("name",)}
	list_display=('id','name')

class CommentAdmin(admin.ModelAdmin):
	list_display=('id','date')

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Comment,CommentAdmin)
