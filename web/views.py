from django.shortcuts import render
from web.models import Event
# Create your views here.

def main(request):
    return render(request,'main.html',{})
def index(request):
    return render(request,'index.html',{})
def pop(request):
    return render(request,'pop.html',{})
def pop2(request):
    return render(request,'pop2.html',{})
def about(request):
    return render(request,'about.html',{})
def goods(request):
    return render(request,'goods.html',{})
def portfolio(request):
    return render(request,'portfolio.html',{})
def portfolio1(request):
    return render(request,'portfolio1.html',{})
def portfolio2(request):
    return render(request,'portfolio2.html',{})
def portfolio3(request):
    return render(request,'portfolio3.html',{})
def portfolio6(request):
    return render(request,'portfolio6.html',{})
def supports(request):
    return render(request,'supports.html',{})
def team(request):
    return render(request,'team.html',{})
def contact(request):
    return render(request,'contact.html',{})
def notice(request):
    datas=Event.objects.all()
    print(len(datas))
    for i in range(len(datas)):
        return render(request,'notice.html',{'content':datas})

