from django.shortcuts import render

# how the page is viewed

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)