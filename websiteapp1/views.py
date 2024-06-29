from django.shortcuts import render
from .models import PediaObject,UserPedia,UserAdmin
import re
# Create your views here.
#CAT VIEWS
def home(request):
    return render(request,'home.html',{'data':'INDIA PEDIA'})
def countries(request):
    result = PediaObject.objects.filter(ObjectTitle='Countries')
    return render(request,'countries.html',{'data':'COUNTIRES','objectdata':result})
def science(request):
    result = PediaObject.objects.filter(ObjectTitle='Science')
    return render(request,'science.html',{'data':'SCIENCE','objectdata':result})
def technology(request):
    result = PediaObject.objects.filter(ObjectTitle='Technology')
    return render(request,'technology.html',{'data':'TECHNOLOGY','objectdata':result})
#FAMOUS VIEWS
def person(request):
    result = PediaObject.objects.filter(ObjectTitle='Person')
    return render(request,'person.html',{'data':'PERSON','objectdata':result})
def songdancemusic(request):
    result = PediaObject.objects.filter(ObjectTitle='SongDanceMusic')
    return render(request,'songdancemusic.html',{'data':'Song,Dance,Music','objectdata':result})
def sports(request):
    result = PediaObject.objects.filter(ObjectTitle='Sports')
    return render(request,'sports.html',{'data':'SPORTS','objectdata':result})
def art(request):
    result = PediaObject.objects.filter(ObjectTitle='Art')
    return render(request,'art.html',{'data':'ART','objectdata':result})
def places(request):
    result = PediaObject.objects.filter(ObjectTitle='Places')
    return render(request,'places.html',{'data':'PLACES','objectdata':result})
def festivals(request):
    result = PediaObject.objects.filter(ObjectTitle='Festivals')
    return render(request,'festivals.html',{'data':'FESTIVALS','objectdata':result})
def parties(request):
    result = PediaObject.objects.filter(ObjectTitle='Parties')
    return render(request,'parties.html',{'data':'POLITICAL PARTIES','objectdata':result})
def culture(request):
    result = PediaObject.objects.filter(ObjectTitle='Culture')
    return render(request,'culture.html',{'data':'CULTURE','objectdata':result})
#features view
def biographies(request):
    result = PediaObject.objects.filter(ObjectTitle='Biographies')
    return render(request,'biographies.html',{'data':'Biographies','objectdata':result})
def onthisday(request):
    result = PediaObject.objects.filter(ObjectTitle='OnThisDay')
    return render(request,'onthisday.html',{'data':'OnThisDay','objectdata':result})
def spotlight(request):
    result = PediaObject.objects.filter(ObjectTitle='Spotlight')
    return render(request,'spotlight.html',{'data':'Spotlight','objectdata':result})
def companionst(request):
    result = PediaObject.objects.filter(ObjectTitle='Companionst')
    return render(request,'companionst.html',{'data':'Companionst','objectdata':result})
def imggal(request):
    result = PediaObject.objects.filter(ObjectTitle='imggal')
    return render(request,'imggal.html',{'data':'ImageGallery','objectdata':result})
def entertainment(request):
    result = PediaObject.objects.filter(ObjectTitle='Entertainment')
    return render(request,'entertainment.html',{'data':'Entertainment','objectdata':result})
def geography(request):
    result = PediaObject.objects.filter(ObjectTitle='Geography')
    return render(request,'geography.html',{'data':'Geography','objectdata':result})

def searchpedia(request):
    searchqry=request.GET['searchstr']
    rst=re.split(',| ', searchqry)
    print(rst)
    result=[]
    for sstr in rst:
        result += PediaObject.objects.filter(ObjectTitle=sstr)
        result += PediaObject.objects.filter(ObjectCat=sstr)
    print(result)
    return render(request,'geography.html',{'data':'Search Result','objectdata':result})
