from django.shortcuts import render, get_object_or_404
from .models import Page

def page(request, id):
    page = get_object_or_404(Page, id=id)
    return render(request, 'pages/sample.html', {'page': page})