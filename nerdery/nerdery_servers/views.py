from django.http import HttpResponse
# from django.shortcuts import render


def home_page(request):
    return HttpResponse('<html><body id="front_page"></body></html>')
