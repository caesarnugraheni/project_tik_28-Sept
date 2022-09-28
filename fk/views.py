from django.shortcuts import render

# Create your views here.
def index(request):
    fk =["Kedokteran", "Keperawatan S1", "Gizi S1", "Ilmu Keolahragaan"]

    konteks = {
        'fk': fk,
    }
    return render (request, 'fk/index.html', konteks)
    
