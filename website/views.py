from django.shortcuts import render


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about-us.html')


def contact_view(request):
    return render(request, 'website/contact.html')

def test_view(request):
    context = {'title': 'aaa', 'content': 'bbb'}
    return render(request, 'website/test.html', context)
# Create your views here.
