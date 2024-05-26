from django.shortcuts import render
from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def single_view(request):
    return render(request, 'blog/single-blog.html')



# Create your views here.
