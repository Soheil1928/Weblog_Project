from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse("home")


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')

    def __str__(self):
        return str(self.user)
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255, default='Click Link Above Post To Read Weblog Post...')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse("article-detail", args=str(self.id))
        return reverse("home")
    
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    
    # def get_absolute_url(self):
    #     return reverse("post-detail", args=str(self.post.pk))

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)