from django.shortcuts import render

# Create your views here.
def pagination(request):
    return render(request,'pagination.html')