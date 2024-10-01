from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'hizmetlerimiz.html')

def about(request):
    return render(request,'hakkimizda.html')

def contact(request):
    return render(request,'iletisim.html')

def sss(request):
    return render(request,'sss.html')
