from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import signup_info
from .models import product_info

from django.contrib.auth.hashers import check_password, make_password
# Create your views here.



def index(request):
    dis_index=product_info.objects.all()
    d1={'all_prod':dis_index}


    return render(request, 'index.html', d1)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    else:
        un = request.POST.get('uname')
        uem = request.POST.get('uemail')
        upass1 = request.POST.get('upass')
        upass = make_password(upass1)
        uadd = request.POST.get('uadd')
        uc = request.POST.get('ucity')
        uv = request.POST.get('uvanue')


        print(un, uem, upass, uadd, uc, uv)

        ds = signup_info(

            user_name=un,
            user_email=uem,
            user_pass=upass,
            address=uadd,
            city=uc,
            vanue=uv

        )

        ds.save()

        return render(request, 'signup.html')



def login(request):
    if request.method=="GET":
        return render(request, 'login.html')
    else:

        user_log=request.POST.get('log_mail')
        pass_log=request.POST.get('log_pass')

        cas=signup_info.match_log(user_log)

        if cas:
            cas_pass=check_password(pass_log, cas.user_pass)
            if cas_pass:
                return HttpResponse("loged in")

            else:
                return HttpResponse("incorrect password")
        else:
            return HttpResponse('incorrect email')


        print(user_log, pass_log)


        return render(request, 'login.html')

