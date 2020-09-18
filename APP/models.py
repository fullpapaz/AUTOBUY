from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.


class Images(models.Model):
    title =models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title


class Car(models.Model):
    title=models.TextField(blank=True, null=True)
    category=models.TextField(blank=True, null=True)
    power=models.IntegerField(blank=True, null=True)
    speed=models.IntegerField(blank=True, null=True)
    model=models.TextField(blank=True, null=True)
    make=models.TextField(blank=True, null=True)
    model_year=models.TextField(blank=True, null=True)
    transmission=models.TextField(blank=True, null=True)
    fuel_type=models.TextField(blank=True, null=True)
    image=models.ManyToManyField(Images)
    condition=models.TextField(blank=True, null=True)
    use_state=models.TextField(blank=True, null=True)
    user=models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    price=models.IntegerField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    slug = models.SlugField()
    paginate_by = 2

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("APP:details", kwargs={
            'slug': self.slug
        })


class Bookmark(models.Model):
    title=models.TextField(blank=True, null=True)
    category=models.TextField(blank=True, null=True)
    power=models.IntegerField(blank=True, null=True)
    speed=models.IntegerField(blank=True, null=True)
    model=models.TextField(blank=True, null=True)
    model_year=models.TextField(blank=True, null=True)
    transmission=models.TextField(blank=True, null=True)
    fuel_type=models.TextField(blank=True, null=True)
    image=models.ImageField(blank=True, null=True)
    condition=models.TextField(blank=True, null=True)
    use_state=models.TextField(blank=True, null=True)
    creator=models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    price=models.IntegerField(blank=True, null=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone=models.CharField(max_length=100, null=True,blank=True)
    USER_TYPE_CHOICES = (
        ('Dealer', 'Dealer'),
        ('Buyer', 'Buyer'),
    )
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)
