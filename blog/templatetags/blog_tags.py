from django import template
from blog.models import Post, Category
from datetime import datetime

register = template.Library()


@register.filter
def snippet(text, args=50):
    return text[:args]


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(args=3):
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now()).order_by('-published_date')[:args]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1, published_date__lte=datetime.now())
    categories = Category.objects.all()

    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
