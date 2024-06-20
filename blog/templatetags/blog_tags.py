from django import template
from blog.models import Post

register = template.Library()


@register.filter
def snippet(text, args=50):
    return text[:args]


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts