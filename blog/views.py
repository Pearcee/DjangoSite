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

def data(request, **kwargs):
    # we will pass this context object into the
    # template so that we can access the data
    # list in the template
    context = {
        'data': [
            {
                'name': 'Celeb 1',
                'worth': '3567892'
            },
            {
                'name': 'Celeb 2',
                'worth': '23000000'
            },
            {
                'name': 'Celeb 3',
                'worth': '1000007'
            },
            {
                'name': 'Celeb 4',
                'worth': '456789'
            },
            {
                'name': 'Celeb 5',
                'worth': '7890000'
            },
            {
                'name': 'Celeb 6',
                'worth': '12000456'
            },
            {
                'name': 'Celeb 7',
                'worth': '896000'
            },
            {
                'name': 'Celeb 8',
                'worth': '670000'
            }
        ]
    }
    template = 'blog/data.html'
    return render(request, template, context)