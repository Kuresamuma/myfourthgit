from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dad(request):
    return HttpResponse("<h1><marquee> I LOVE MY DAD</h1></marquee>")
