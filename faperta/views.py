from django.shortcuts import render

# Create your views here.
def faperta(request):
    faperta =["Agribisnis", "Agroekoteknologi", "Ilmu Perikanan", "Teknologi Pangan"]

    konteks = {
        'faperta': faperta,
    }
    return render(request, 'index.html', konteks)
