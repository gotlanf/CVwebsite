from django.db import models
from django_jalali.db import models as jmodels
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = jmodels.jDateTimeField(null=True, blank=True)

    def get_next(self):
        return Post.objects.filter(id__gt=self.id).order_by('id').first()

    def get_previous(self):
        return Post.objects.filter(id__lt=self.id).order_by('-id').first()

    def __str__(self):
        return self.title


class Meta:
    ordering = ['created_date']
