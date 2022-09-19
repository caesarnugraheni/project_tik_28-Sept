from django.shortcuts import render

# Create your views here.
def fh(request):
    fh =["Ilmu Hukum"]

    konteks = {
        'fh': fh,
    }
    return render(request, 'index2.html', konteks)
