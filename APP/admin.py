from django.contrib import admin
from .models import Car,Images,Bookmark,UserProfile,Article

# Register your models here.
admin.site.register(Car)
admin.site.register(Images)
admin.site.register(Bookmark)
admin.site.register(UserProfile)
admin.site.register(Article)
