from django.shortcuts import render

# Create your views here.
def feb(request):
    feb =["Sarjana Manajemen", "Sarjana Akuntansi", "Sarjana Ekonomi Syariah", "Sarjana Ilmu Ekonomi Pembangunan"]

    konteks = {
        'feb': feb,
    }
    return render(request, 'index1.html', konteks)

    
