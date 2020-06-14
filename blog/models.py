from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length = 255)
    body = models.TextField()
    slug = models.CharField(max_length= 100)
    created_on = models.DateTimeField(auto_now_add= True)
    last_modified = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField('Category', related_name = 'posts')
    def __str__(self):
        return 'POST is ' + self.title

class Comment(models.Model):
    author = models.CharField(max_length = 60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete= models.CASCADE)
    def __str__(self):
        return 'Comment made by ' + self.author

class Contact(models.Model):
    email = models.CharField(max_length= 50)
    subject = models.CharField(max_length= 150)
    message = models.TextField()
    def __str__(self):
        return 'Message from ' + self.email

class Newsletter(models.Model):
    email= models.CharField(max_length= 20)
    def __str__(self):
        return 'New Email added '+ self.email



