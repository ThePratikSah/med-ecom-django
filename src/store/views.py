from django.shortcuts import render


# Create your views here.
def get_store(request):
    return render(request, "index.html")
