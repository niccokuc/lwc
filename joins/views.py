from django.shortcuts import render
from .forms import JoinForm
from .models import Join

# how the page is viewed
def home(request):
    #print(request.POST)

    # This is usign regualr Django forms
    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     email = form.cleaned_data['email']
    #     new_join, created = Join.objects.get_or_create(email=email)
    #     print(new_join)
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)

    context = {"form": form}
    template = 'home.html'
    return render(request, template, context)