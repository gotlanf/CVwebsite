from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone


def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=now)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    post.counted_view += 1  # افزایش تعداد بازدید
    post.save()  # ذخیره‌سازی تغییرات
    context = {'post': post}
    return render(request, 'blog/single-blog.html', context)

# Create your views here.
