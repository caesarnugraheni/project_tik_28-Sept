from django.shortcuts import render

# Create your views here.
def index(request):
    feb =["Sarjana Manajemen", "Sarjana Akuntansi", "Sarjana Ekonomi Syariah", "Sarjana Ilmu Ekonomi Pembangunan"]

    konteks = {
        'feb': feb,
    }
    return render(request, 'feb/index.html', konteks)

    
