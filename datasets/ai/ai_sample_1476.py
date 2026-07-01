# formA.py
from django.forms import ModelForm
from .models import TableA

class formA(ModelForm):
    class Meta:
        model = TableA
        fields = ['field1','field2','field3','field4']

# formB.py
from django.forms import ModelForm
from .models import TableB

class formB(ModelForm):
    class Meta:
        model = TableB
        fields = ['field1','field2','field3','field4']

# views.py
from django.shortcuts import render
from .forms import formA, formB

def form_view(request):
    formA_data = formA(request.POST or None)
    formB_data = formB(request.POST or None)
    if formA_data.is_valid() and formB_data.is_valid():
        formA_data.save()
        formB_data.save()
        return render(request, 'thankyoupage.html')
    return render(request, 'formpage.html', {'formA':formA_data, 'formB':formB_data})