from django.shortcuts import render
from dosen.models import dosen
from dosen.forms import FormDosen

# Create your views here.
def index(request):
    
    dosens = dosen.objects.all()
    # dosens = dosen.objects.filter(prodi='Pendidikan Matematika')

    variabel = {
        'dosens' : dosens,
    }
    return render(request, 'dosen/index.html', variabel)


def tambah_dosen(request):
    if  request.POST:
        form = FormDosen(request.POST)
        
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'dosen/tambah-dosen.html', konteks)
        else:
            print("ADA YANG SALAH")

            konteks = {
                'form' : form,
            }
            return render(request, 'dosen/tambah-dosen.html', konteks)
            
    else:
        form = FormDosen()

        konteks = {
            'form': form,
        }
        return render(request, 'dosen/tambah-dosen.html', konteks)