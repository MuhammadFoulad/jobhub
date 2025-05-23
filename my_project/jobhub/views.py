from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from jobhub.models import *
from jobhub.utils import *

# Create your views here.

def user_registration_get(request):
    return render(request,"user_registration_page.html")


def user_registration_post(request):
    email=request.POST['email']
    phone=request.POST['phone']
    name=request.POST['name']
    password=request.POST['password']
    isUserExist= Users.objects.filter(Q(email=email) | Q(phone=phone)).exists()
    if isUserExist:
        return HttpResponse('''<script>alert("email or phone number is already exist");window.location="/login_get/"</script>''')
    salt=generate_random_string(7)
    password=password+salt
    password=encript_password(password)
    login_id=save_login(email,password,salt,phone)
    save_user(name,password,email,phone,login_id)
    return HttpResponse('''<script>alert("user registration is successfull,now you can login");window.location="/login_get/"</script>''')

def login_get(request):
    return render(request,"login_page.html")

def login_post(request):
    emailorphone=request.POST['emailorphone']
    password=request.POST['password']
    login=Login.objects.filter(Q(email=emailorphone) | Q(phone=emailorphone))
    if login:
        login=Login.objects.get(Q(email=emailorphone) | Q(phone=emailorphone))
        salt=login.salt
        password=password+salt
        password=encript_password(password)
        if login.password==password:
            request.session['lid']=login.id
            if login.type=="user":
                return HttpResponse('''<script>alert("login successfull");window.location="/user_registration_get/"</script>''')
            elif login.type=="company":
                return HttpResponse('''<script>alert("login successfull");window.location="/user_registration_get/"</script>''')
        else:
            return HttpResponse('''<script>alert("password is incorrect");window.location="/login_get/"</script>''')    
    else:
        return HttpResponse('''<script>alert("Invalid email or phone user not exist.Please try again");window.location="/login_get/"</script>''')    




        
      
    