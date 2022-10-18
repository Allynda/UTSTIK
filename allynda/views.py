from django.shortcuts import render

# Create your views here.
def indexallynda(request):
    return render(request, 'allynda.html')