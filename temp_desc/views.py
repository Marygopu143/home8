from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    user = User.objects.get(username="mary")
    context = {"page_title": "Home Page", "user": user}
    return render(request, "index.html", context)
