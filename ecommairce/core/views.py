from django.shortcuts import render

# Create your views here.

def frontpage(request):
    template = 'frontpage.html'
    ctx = {
        'curant': 'home'
    }
    return render(request, template, ctx)
