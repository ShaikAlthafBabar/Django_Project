from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User



class streamingPlatform(models.Model):
    platform=models.CharField(max_length=100)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    def __str__(self):
        return self.platform

# Create your models here.
class watchList(models.Model):
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    platform=models.ForeignKey(streamingPlatform,on_delete=models.CASCADE,related_name="watchlist")
    active=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    total_ratings=models.IntegerField(default=0)
    avg_rating=models.FloatField(default=0)

    def __str__(self):
        return self.title

class Review(models.Model):
     review_user=models.ForeignKey(User,on_delete=models.CASCADE)
     rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
     description=models.CharField(max_length=200,null=True)
     created=models.DateTimeField(auto_now_add=True)
     update=models.DateTimeField(auto_now=True)
     active=models.BooleanField(default=True)
     movie=models.ForeignKey(watchList,on_delete=models.CASCADE,related_name='review')
     
     def __str__(self):
        return str(self.rating)+'-'+self.movie.title