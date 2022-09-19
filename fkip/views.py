from django.shortcuts import render

# Create your views here.
def fkip(request):
    fkip =["Pendidikan Matematika", "Pendidikan Bahasa Inggris", "Pendidikan Sosiologi", "Pendidikan Bahasa Indonesia", "Pendidikan Non Formal", "Pendidikan Biologi", "Pendidikan Guru PAUD", "Pendidikan Guru Sekolah Dasar", "Pendidikan Bimbingan dan Konseling", "Pendidikan Sejarah"]

    konteks = {
        'fkip': fkip,
    }
    return render(request, 'index4.html', konteks)
