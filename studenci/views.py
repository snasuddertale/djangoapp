from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from studenci.models import Miasto, Uczelnia
from studenci.forms import UserLoginForm, UserUczelniaForm

def index(request):
    return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    # return render(request,'pizza/index.html')


def miasta(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        kod = request.POST.get('kod', '')
        if len(nazwa.strip()) and len(kod.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Poprawnie dodano dane!")
        else:
            messages.error(request, "Niepoprawne dane!")

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta}
    return render(request, 'studenci/miasta.html', kontekst)


def uczelnie(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa', '')
        u = Uczelnia(nazwa=nazwa)
        u.save()

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie}
    return render(request, 'studenci/uczelnie.html', kontekst)

def loguj_studenta(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'studenci/login.html', kontekst)

def dodaj_uczelnie(request):
    if request.method == 'POST':
        pass
    else:
        form = UserUczelniaForm()
    kontekst = {'form': form}
    return render(request, 'studenci/uczelnia.html', kontekst)