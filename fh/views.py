from django.shortcuts import render

# Create your views here.
def index(request):
    fh =["Ilmu Hukum"]

    konteks = {
        'fh': fh,
    }
    return render(request, 'fh/index.html', konteks)
