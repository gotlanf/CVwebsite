from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from datetime import datetime


# Create your views here.

def blog_view(request, cat_name=None):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=now)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    next_post = post.get_next()
    previous_post = post.get_previous()
    post.counted_view += 1  # افزایش تعداد بازدید
    post.save()  # ذخیره‌سازی تغییرات
    context = {'post': post,
               'next_post': next_post,
               'previous_post': previous_post, }
    return render(request, 'blog/single-blog.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=True, published_date__lte=datetime.now()).order_by('-published_date')
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)
