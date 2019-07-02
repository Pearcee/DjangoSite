from django.shortcuts import render

# Create your views here.


def about(request):
    template = 'blog/about.html'
    return render(request, template)


def contact(request):
    template = 'blog/contact.html'
    return render(request, template)


def index(request):
    template = 'blog/index.html'
    return render(request, template)
