from django.shortcuts import render

# Create your views here.
def fk (request):
    fk =["Kedokteran", "Keperawatan S1", "Gizi S1", "Ilmu Keolahragaan"]

    konteks = {
        'fk': fk,
    }
    return render (request, 'index3.html', konteks)
    
