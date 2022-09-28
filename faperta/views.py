from django.shortcuts import render

# Create your views here.
def index(request):
    faperta =["Agribisnis", "Agroekoteknologi", "Ilmu Perikanan", "Teknologi Pangan"]

    konteks = {
        'faperta': faperta,
    }
    return render(request, 'faperta/index.html', konteks)
