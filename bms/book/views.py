from django.shortcuts import render

# Create your views here.
def books(req):
    return render(req,'index.html')
def demo(req):
    return render(req,'demo.html')