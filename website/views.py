from django.shortcuts import render


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about-us.html')


def contact_view(request):
    return render(request, 'website/contact.html')

# Create your views here.
