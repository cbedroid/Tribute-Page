from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class DateTime(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    main_content = models.TextField(max_length=5000)
    second_content = models.TextField(max_length=5000,blank=True,null=True)
    third_content = models.TextField(max_length=5000,blank=True,null=True)

    def __str__(self):
        return self.headline

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Blog(DateTime):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False,null=False)
    subtitle = models.CharField(max_length=150, blank=False,null=False)
    image = models.ImageField(upload_to="assets/images", blank=False,null=False)
    image_title = models.CharField(max_length=150, blank=True,null=True)
    status = models.IntegerField(choices=STATUS,default=0)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    slug = models.SlugField(editable=False,unique=True)

    class Meta:
        ordering = ['-created']

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("core:blog-detail",kwargs={
            'slug': self.slug,
        })

    def __str__(self):
        return self.title