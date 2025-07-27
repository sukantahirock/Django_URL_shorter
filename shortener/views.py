from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
from django.http import HttpResponse

def index(request):
    short_url = None
    if request.method == "POST":
        original = request.POST.get("url")
        obj, created = ShortURL.objects.get_or_create(original_url=original)
        short_url = request.build_absolute_uri(f"/{obj.short_code}")
    return render(request, "shortener/index.html", {"short_url": short_url})

def redirect_to_original(request, code):
    obj = get_object_or_404(ShortURL, short_code=code)
    return redirect(obj.original_url)
