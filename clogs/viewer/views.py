from django.shortcuts import render

# Create your views here.


def viewer(request):
    return render(request, "index.html")
