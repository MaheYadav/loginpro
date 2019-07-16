from django.shortcuts import render
from .foms import Registrationform
def registration_view(request):
    if request.method == 'POST':
        rform= Registrationform(request.POST)
        if rform.is_valid():
            rform.save()
            rform=Registrationform
            return render(request,'reg.html',{'rform':rform})

    else:
        rform = Registrationform
        return render(request, 'reg.html', {'rform': rform})