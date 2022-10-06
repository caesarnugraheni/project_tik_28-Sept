from django.forms import ModelForm
from django import forms
from dosen.models import dosen


class FormDosen(ModelForm):
    class Meta:
        model = dosen
        exclude = ['foto']
        # fields = '__all__'
    # bisa hanya menuliskan nama saja atau gimana pake ['nama', 'ttl']

        widgets = {
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'ttl' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }
#  widgetsnya udah jalan
