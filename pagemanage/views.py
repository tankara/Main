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

teachers_list = [
    {"name":"cafer",
     "branch":"kimya",
     "exp": 10,
     "pic":"https://picsum.photos/id/237/200/300"
     },
     {"name":"selahattin",
     "branch":"edebiyat",
     "exp": 7,
     "pic":"https://picsum.photos/id/237/200/300"
     },
     {"name":"pınar",
     "branch":"fizik",
     "exp": 2,
     "pic":"https://picsum.photos/id/237/200/300"
     },
     {"name":"ibrahim",
     "branch":"ilkokul",
     "exp": 30,
     "pic":"https://picsum.photos/id/237/200/300"
     }
]

def teachers(request):
    data= {
        "teachers": teachers_list
    }
    return render(request,'teachers.html',data)
