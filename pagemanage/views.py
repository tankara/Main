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

def sss(request):
    return render(request,'sss.html')

def teachers(request):
    data= {
    }
    return render(request,'teachers.html',data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        message = request.POST.get('message')
        
        # Burada form verilerini işleyebilir, e-posta gönderebilir veya veritabanına kaydedebilirsiniz
        
        return render(request, 'iletisim.html', {
            'success': True,
            'message': 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapacağız.'
        })
        
    return render(request, 'iletisim.html', {
        'page_title': 'İletişim',
        'contact_info': {
            'address': 'Örnek Mahallesi, Örnek Sokak No:1 Kadıköy/İstanbul',
            'phone': '+90 (212) 123 45 67',
            'email': 'info@example.com',
            'working_hours': 'Pazartesi - Cumartesi: 09:00 - 18:00'
        }
    })

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('rememberMe')
        
        # Burada giriş işlemleri yapılacak
        
        return render(request, 'login.html', {
            'success': True,
            'message': 'Başarıyla giriş yaptınız.'
        })
        
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        # Şifre kontrolü
        if password != password2:
            return render(request, 'signup.html', {
                'error': True,
                'message': 'Şifreler eşleşmiyor.'
            })
            
        # Burada kayıt işlemleri yapılacak
        
        return render(request, 'signup.html', {
            'success': True,
            'message': 'Hesabınız başarıyla oluşturuldu.'
        })
        
    return render(request, 'signup.html')
