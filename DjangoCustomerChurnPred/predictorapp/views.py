from django.shortcuts import render

# Create your views here.
def predict(request):
    return render(request,"predictorapp/index.html")
