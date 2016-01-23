from django.shortcuts import render
from .forms import EmailForm
from .models import Join

# how the page is viewed
def home(request):
    #print(request.POST)
    form = EmailForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        new_join, created = Join.objects.get_or_create(email=email)
        print(new_join)
    context = {"form": form}
    template = 'home.html'
    return render(request, template, context)