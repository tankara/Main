from django.shortcuts import render

services_list = [
    {"name":"Birebir Çevrimiçi Özel Dersler",
     "explanation":"Çevrimiçi oturumlar sırasında bir öğretmen ve bir öğrenci tarafından işlenen dersler.",
     "pic":"img/birebir.png"
     },
     {"name":"Grup Çevrimiçi Özel Dersler",
     "explanation":"Çevrimiçi oturumlar sırasında bir öğretmen ve aynı seviyedeki öğrenciler tarafından işlenen dersler.",
     "pic":"img/grup.png"
     },
]

def index(request):
    return render(request,'index.html')

def services(request):
    data = {
        "services":services_list
    }
    return render(request,'hizmetlerimiz.html',data)

def about(request):
    return render(request,'hakkimizda.html')

def contact(request):
    return render(request,'iletisim.html')

def sss(request):
    return render(request,'sss.html')

def teachers(request):
    data= {
    }
    return render(request,'teachers.html',data)
