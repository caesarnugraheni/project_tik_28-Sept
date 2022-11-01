from django.shortcuts import render, redirect
from dosen.models import dosen
from dosen.forms import FormDosen
from django.contrib import messages

def hapus_dosen(request, id_dosen):
    dosen1 = dosen.objects.filter(id=id_dosen)
    dosen1.delete()

    return redirect('/dosen/')

def ubah_dosen(request, id_dosen):
    dosenz = dosen.objects.get(id=id_dosen)
    template = 'dosen/ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosenz)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui!!")
            return redirect('ubah_dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosenz)
        kontek = {
            'form':form,
            'dosenz':dosenz,
        }
    return render(request, template, kontek)


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