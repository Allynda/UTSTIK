from django.shortcuts import render

# Create your views here.
def indexbarisanbilangan(request):
    return render(request, 'barisanbilangan.html')