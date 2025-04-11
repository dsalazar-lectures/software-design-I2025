from django.shortcuts import render

# Create your views here.
items = [
    {"label": "Home", "url_name": "home"},
    {"label": "About", "url_name": "about"},
    {"label": "Contact", "url_name": "contact"},
]

def index(request):
    context = {
        "site_name": "JJSite",
        "items": items,
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "site_name": "JJSite",
        "items": items,
    }
    return render(request, "about.html", context)

def contact(request):
    context = {
        "site_name": "JJSite",
        "items": items,
    }
    return render(request, "contact.html", context)