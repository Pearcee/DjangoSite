from django.shortcuts import render

# Create your views here.


def index(request):
    template = 'blog/index.html'
    return render(request, template)
