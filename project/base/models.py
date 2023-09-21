from django.db import models
from django.contrib.auth.models import AbstractUser


POST_CHOICES = (
    ('PASTOR', 'PASTOR'), 
    ('PREACHER', 'PREACHER'),
    ('MEMBER', 'MEMBER')
)

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    post = models.CharField(max_length=200, null=True, choices=POST_CHOICES)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, upload_to='images')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email
    


class Artist(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    country = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    image= models.ImageField(upload_to='images', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)


    def __str__(self):
         return self.title
    
    class Meta:
        ordering = ['-updated', '-updated']
         

class Song(models.Model):
    # artist= models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    title= models.CharField(max_length=200)
    image= models.ImageField(upload_to='images')
    audio_file = models.FileField(blank=True,null=True, upload_to='songs/')
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    # duration=models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated', '-created']



class Sermon(models.Model):
    host = models.CharField(max_length=200)
    post = models.CharField(max_length=200, null=True, choices=POST_CHOICES)
    title= models.CharField(max_length=200)
    image= models.ImageField(upload_to='images')
    audio_file = models.FileField(blank=True,null=True, upload_to='songs/')
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-updated', '-created']



class Testimony(models.Model):
    name = models.CharField(max_length=200)
    image= models.ImageField(upload_to='images')
    audio_file = models.FileField(blank=True,null=True, upload_to='songs/')
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    

    class Meta:
        ordering = ['-updated', '-created']


class MusicFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music = models.ForeignKey(Song, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.music.title